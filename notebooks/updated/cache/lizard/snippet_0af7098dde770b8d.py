def remove_handler(self, handler):
    try:
        self._events[handler.type].remove(handler)
        return True
    except ValueError:
        return False