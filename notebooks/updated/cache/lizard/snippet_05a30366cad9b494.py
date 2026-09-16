def back_off_until(self):
    if self._back_off_until is None:
        return None
    with self._back_off_lock:
        if self._back_off_until is None:
            return None
        if self._back_off_until < datetime.datetime.now():
            self._back_off_until = None
            return None
        return self._back_off_until