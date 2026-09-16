def get_data(self):
    fifo_int_size_1 = self.FIFO_INT_SIZE
    fifo_int_size_2 = self.FIFO_INT_SIZE
    if fifo_int_size_1 > fifo_int_size_2:
        fifo_int_size = fifo_int_size_2
        logger.warning('Reading wrong FIFO size. Expected: %d <= %d' % (
            fifo_int_size_1, fifo_int_size_2))
    else:
        fifo_int_size = fifo_int_size_1
    return np.frombuffer(self._intf.read(self._conf['base_data_addr'], size
        =4 * fifo_int_size), dtype=np.dtype('<u4'))