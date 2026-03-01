# machine/terminal_socket.py
import logging
import socket
from threading import Thread

from flask import session, request
from flask_socketio import SocketIO, disconnect

import settings

log = logging.getLogger(__name__)

socketio = SocketIO(async_mode="threading")

docker_sessions = {}


def _get_raw_socket(obj):
    if obj is None:
        return None

    if hasattr(obj, "recv"):
        return obj

    if isinstance(obj, tuple) and obj:
        obj = obj[0]

    if hasattr(obj, "_sock"):
        return obj._sock

    return None


def _reader_thread(sid, sock):
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                break

            socketio.emit(
                "terminal_output",
                data.decode("utf-8", errors="replace"),
                room=sid,
            )
    except Exception:
        pass
    finally:
        cleanup_session(sid)


def cleanup_session(sid: str):
    ds = docker_sessions.pop(sid, None)
    if not ds:
        return

    sock = ds.get("sock")
    if not sock:
        return

    try:
        try:
            sock.shutdown(socket.SHUT_RDWR)
        except Exception:
            pass
        sock.close()
    except Exception:
        pass


@socketio.on("terminal_connect")
def terminal_connect(data):
    user_id = session.get("user_id")
    container_name = data.get("container")

    if not user_id or not container_name:
        disconnect()
        return

    containers = settings.CLIENT.containers.list(
        all=True,
        filters={
            "name": container_name,
            "label": [f"user_id={user_id}", "managed=true"],
        },
    )

    if not containers:
        disconnect()
        return

    container = containers[0]

    if container.status != "running":
        container.start()

    # Create interactive bash session
    exec_id = settings.CLIENT.api.exec_create(
        container.id,
        cmd="/bin/bash",
        stdin=True,
        tty=True,
    )["Id"]

    raw = settings.CLIENT.api.exec_start(
        exec_id,
        tty=True,
        socket=True,
    )

    sock = _get_raw_socket(raw)
    if not sock:
        disconnect()
        return

    if isinstance(sock, socket.socket):
        sock.setblocking(True)

    docker_sessions[request.sid] = {
        "sock": sock,
        "exec_id": exec_id,
    }

    Thread(
        target=_reader_thread,
        args=(request.sid, sock),
        daemon=True,
    ).start()


@socketio.on("terminal_input")
def terminal_input(data):
    ds = docker_sessions.get(request.sid)
    if not ds:
        return

    sock = ds["sock"]

    if isinstance(data, str):
        data = data.encode("utf-8")

    try:
        sock.sendall(data)
    except Exception:
        cleanup_session(request.sid)


@socketio.on("resize")
def resize(data):
    ds = docker_sessions.get(request.sid)
    if not ds:
        return

    rows = int(data.get("rows", 24))
    cols = int(data.get("cols", 80))

    try:
        settings.CLIENT.api.exec_resize(
            ds["exec_id"],
            height=rows,
            width=cols,
        )
    except Exception:
        pass


@socketio.on("disconnect")
def on_disconnect():
    cleanup_session(request.sid)