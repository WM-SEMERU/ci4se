def _init_ctable(self, path):
    sid_containing_dirname = os.path.dirname(path)
    if not os.path.exists(sid_containing_dirname):
        os.makedirs(sid_containing_dirname)
    initial_array = np.empty(0, np.uint32)
    table = ctable(rootdir=path, columns=[initial_array, initial_array,
        initial_array, initial_array, initial_array], names=['open', 'high',
        'low', 'close', 'volume'], expectedlen=self._expectedlen, mode='w')
    table.flush()
    return table