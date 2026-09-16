def on_button(callback, args=(), buttons=(LEFT, MIDDLE, RIGHT, X, X2),
    types=(UP, DOWN, DOUBLE)):
    if not isinstance(buttons, (tuple, list)):
        buttons = buttons,
    if not isinstance(types, (tuple, list)):
        types = types,

    def handler(event):
        if isinstance(event, ButtonEvent):
            if event.event_type in types and event.button in buttons:
                callback(*args)
    _listener.add_handler(handler)
    return handler