def keyevent2tuple(event):
    return event.type(), event.key(), event.modifiers(), event.text(
        ), event.isAutoRepeat(), event.count()