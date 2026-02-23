""" - Before request handler
 -- All handlers MUST start with before_request_ and be callable"""


before_request = []

for name in list(globals().keys()):
    if name.startswith("before_request_") and callable(globals()[name]):
        before_request.append(globals()[name])