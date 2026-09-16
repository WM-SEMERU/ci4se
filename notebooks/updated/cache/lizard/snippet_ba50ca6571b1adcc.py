def lock(self, name, timeout=None, sleep=0.1, blocking_timeout=None,
    lock_class=None, thread_local=True):
    if lock_class is None:
        if self._use_lua_lock is None:
            try:
                LuaLock.register_scripts(self)
                self._use_lua_lock = True
            except ResponseError:
                self._use_lua_lock = False
        lock_class = self._use_lua_lock and LuaLock or Lock
    return lock_class(self, name, timeout=timeout, sleep=sleep,
        blocking_timeout=blocking_timeout, thread_local=thread_local)