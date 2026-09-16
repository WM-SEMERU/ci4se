def storage_type(self):
    nf = np.load(str(self.path), mmap_mode='c', allow_pickle=False)
    if np.iscomplexobj(nf):
        st = 'field'
    else:
        st = 'phase'
    return st