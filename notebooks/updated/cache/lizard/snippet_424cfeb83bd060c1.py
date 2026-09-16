def argmax(self):
    if 'argmax' not in self.attrs.keys():

        def f(dataset, s):
            arr = dataset[s]
            try:
                amin = np.nanargmax(arr)
            except ValueError:
                amin = 0
            idx = np.unravel_index(amin, arr.shape)
            val = arr[idx]
            return tuple(i + (ss.start if ss.start else 0) for i, ss in zip
                (idx, s)), val
        chunk_res = self.chunkwise(f)
        idxs = [i[0] for i in chunk_res.values()]
        vals = [i[1] for i in chunk_res.values()]
        self.attrs['argmax'] = idxs[np.nanargmax(vals)]
    return tuple(self.attrs['argmax'])