def get_reporter_state():
    frame = sys._getframe(3)
    reporter = frame.f_locals['self']
    line_number = frame.f_locals['line_number']
    offset = frame.f_locals['offset']
    text = frame.f_locals['text']
    check = frame.f_locals['check']
    return reporter, line_number, offset, text, check