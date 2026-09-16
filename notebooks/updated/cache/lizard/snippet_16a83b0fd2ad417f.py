def dump(cls):
    with cls.lock:
        if not cls.instances:
            return
        atexit.unregister(cls.dump)
        cls._pre_dump()
        for self in cls.instances.values():
            self._dump()
        cls._post_dump()