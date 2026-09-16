def save_trajs(trajs, fn, meta, key_to_path=None):
    if key_to_path is None:
        key_to_path = default_key_to_path
    validate_keys(meta.index, key_to_path)
    backup(fn)
    os.mkdir(fn)
    for k in meta.index:
        v = trajs[k]
        npy_fn = os.path.join(fn, key_to_path(k))
        os.makedirs(os.path.dirname(npy_fn), exist_ok=True)
        np.save(npy_fn, v)