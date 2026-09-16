def read_message(self):
    with self.__class__.__locker:
        result = self.__passive_read(4)
        if result is None:
            return None
        four_bytes, last_buffer_index, updates1 = result
        length, = unpack('>I', four_bytes)
        result = self.__passive_read(length, last_buffer_index)
        if result is None:
            return None
        data, last_buffer_index, updates2 = result
        for updates in (updates1, updates2):
            for update in updates:
                buffer_index, buffer_, length_consumed = update
                self.__buffers[buffer_index] = buffer_ if buffer_ else ''
                self.__length -= length_consumed
        self.__read_buffer_index = last_buffer_index
        self.__hits += 1
        if self.__hits >= self.__class__.__cleanup_interval:
            self.__cleanup()
            self.__hits = 0
    return data