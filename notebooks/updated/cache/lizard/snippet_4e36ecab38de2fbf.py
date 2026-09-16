def read(self):

    def warn(msg, elapsed_time, current_time):
        desc = self._cache_id_desc()
        self._warnings('{0} {1}: {2}s < {3}s', msg, desc, elapsed_time,
            current_time)
    file_time = get_time()
    out = self._out
    if out is None:
        if self.verbose:
            self._warnings('reading {0} from disk', self._cache_id_desc())
        with open(self._cache_file, 'rb') as f_in:
            out = None
            while True:
                t_out = f_in.read(CHUNK_SIZE)
                if not len(t_out):
                    break
                if out is not None:
                    out += t_out
                else:
                    out = t_out
            self._out = out
    cache_id_obj, elapsed_time, res = self._read(out)
    self.ensure_cache_id(cache_id_obj)
    real_time = get_time() - file_time
    if elapsed_time is not None and real_time > elapsed_time:
        warn('reading cache from disk takes longer than computing!',
            elapsed_time, real_time)
    elif self._start_time is not None and elapsed_time is not None:
        current_time = get_time() - self._start_time
        if elapsed_time < current_time:
            warn('reading cache takes longer than computing!', elapsed_time,
                current_time)
    self._last_access = get_time()
    return res