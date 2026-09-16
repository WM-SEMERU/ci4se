def save(self, fname, compression='blosc'):
    if hasattr(self, 'dtype'):
        if 'list' in self.dtype:
            data = np.array(self.data)
        elif 'df' in self.dtype:
            data = {k: np.array(v).astype('str') for k, v in self.data.
                to_dict('list').items()}
        else:
            data = self.data
    geo = {'data': data, 'xform_data': np.array(self.xform_data), 'reduce':
        self.reduce, 'align': self.align, 'normalize': self.normalize,
        'semantic': self.semantic, 'corpus': np.array(self.corpus) if
        isinstance(self.corpus, list) else self.corpus, 'kwargs': self.
        kwargs, 'version': self.version, 'dtype': self.dtype}
    if fname[-4:] != '.geo':
        fname += '.geo'
    dd.io.save(fname, geo, compression=compression)