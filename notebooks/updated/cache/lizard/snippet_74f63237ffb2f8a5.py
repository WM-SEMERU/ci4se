def map_tqdm(self):
    with Pool(self.cpu_count) as pool:
        vals = [v for v in tqdm(pool.imap_unordered(self._func, self.
            _iterable), total=len(self._iterable))]
        pool.close()
        return vals