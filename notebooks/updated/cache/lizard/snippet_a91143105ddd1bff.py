def for_window(cls, window):
    utcnow = datetime.datetime.utcnow()
    return cls(utcnow - window, 0)