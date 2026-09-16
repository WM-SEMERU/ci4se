def add_cache_entry(self, key, entry):
    copied_entry = copy.copy(entry)
    self._memory_overlay[key] = copied_entry
    if self._user_db_path is not None:
        asyncio.ensure_future(asyncio.get_event_loop().run_in_executor(None,
            writeback, self._user_db_path / key.path, entry.captured_events))