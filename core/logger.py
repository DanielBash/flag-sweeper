""" - Logging settings
- Colorful logs and formatting"""

# -- importing modules
import datetime
import logging
import pprint
import shutil

from rich.console import Console
from rich.traceback import install
import flask.cli

# -- settings cleaner tracebacks
install()

# -- logging setup
console = Console(force_terminal=True, color_system="truecolor", legacy_windows=False,
                  width=shutil.get_terminal_size().columns * 2)


# - base log class
class RichMetaHandler(logging.Handler):
    def emit(self, record):
        time = datetime.datetime.fromtimestamp(record.created).strftime("%H:%M:%S")
        level = record.levelname
        msg = record.getMessage()
        file = record.filename
        line = record.lineno

        console.print(
            f"[dim]{time}[/] "
            f"[bold cyan]{level:<7}[/] "
            f"[magenta]{file}:{line}[/] "
            f"{msg}",
            markup=True
        )


# - rich print, without a lot of info
def rich(msg):
    console.print(msg, markup=True)


handler = RichMetaHandler()
log = logging.getLogger("flagsweeper")
log.setLevel(logging.DEBUG)
log.addHandler(handler)
log.propagate = False
log.rich = rich