def add(self, crash, allow_duplicates=True):
    if not allow_duplicates:
        signature = pickle.dumps(crash.signature, protocol=0)
        if self._session.query(CrashDTO.id).filter_by(signature=signature
            ).count() > 0:
            return
    crash_id = self.__add_crash(crash)
    self.__add_memory(crash_id, crash.memoryMap)
    crash._rowid = crash_id