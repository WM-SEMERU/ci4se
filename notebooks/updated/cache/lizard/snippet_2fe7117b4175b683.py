def _convert_results(self, data, **kwargs):
    if kwargs.get('multiprocessing', False):
        m = mp.Manager()
        output = m.Queue()
        pdb.set_trace()
        pool = mp.Pool(processes=pool_size)
        for i, row in enumerate(data):
            for key, val in row.items():
                try:
                    pool.apply(convert_row_main, args=(val, i, key, output))
                except:
                    pass
        for item in output:
            pdb.set_trace()
        return output
    else:
        return [{key: pyrdf(value) for key, value in row.items()} for row in
            data]