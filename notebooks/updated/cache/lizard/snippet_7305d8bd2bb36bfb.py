def close_cursor(self, cursor_id, address=None):
    if not isinstance(cursor_id, integer_types):
        raise TypeError('cursor_id must be an instance of (int, long)')
    if self.__cursor_manager is not None:
        self.__cursor_manager.close(cursor_id, address)
    else:
        self.__kill_cursors_queue.append((address, [cursor_id]))