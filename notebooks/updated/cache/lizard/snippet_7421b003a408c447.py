def from_paths(cls, path, bs=64, tfms=(None, None), trn_name='train',
    val_name='valid', test_name=None, test_with_labels=False, num_workers=8):
    assert not (tfms[0] is None or tfms[1] is None
        ), 'please provide transformations for your train and validation sets'
    trn, val = [folder_source(path, o) for o in (trn_name, val_name)]
    if test_name:
        test = folder_source(path, test_name
            ) if test_with_labels else read_dir(path, test_name)
    else:
        test = None
    datasets = cls.get_ds(FilesIndexArrayDataset, trn, val, tfms, path=path,
        test=test)
    return cls(path, datasets, bs, num_workers, classes=trn[2])