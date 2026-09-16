def pause_unit(assess_status_func, services=None, ports=None, charm_func=None):
    _, messages = manage_payload_services('pause', services=services,
        charm_func=charm_func)
    set_unit_paused()
    if assess_status_func:
        message = assess_status_func()
        if message:
            messages.append(message)
    if messages and not is_unit_upgrading_set():
        raise Exception("Couldn't pause: {}".format('; '.join(messages)))