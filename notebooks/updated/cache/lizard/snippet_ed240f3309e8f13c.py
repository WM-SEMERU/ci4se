def question(title='', text='', width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT,
    timeout=None):
    response = _simple_dialog(Gtk.MessageType.QUESTION, text, title, width,
        height, timeout)
    if response == Gtk.ResponseType.YES:
        return True
    elif response == Gtk.ResponseType.NO:
        return False
    return None