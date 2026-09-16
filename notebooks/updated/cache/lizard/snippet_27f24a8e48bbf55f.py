def abort(err):
    if _debug:
        abort._debug('abort %r', err)
    global local_controllers
    for controller in local_controllers.values():
        controller.abort(err)