def save_retinotopy_cache(sdir, sid, hemi, props, alignment='MSMAll',
    overwrite=False):
    h = hemi[:2]
    htype = hemi.split('_')[1]
    if (_auto_download_options is None or 'retinotopy_cache' not in
        _auto_download_options or not _auto_download_options[
        'retinotopy_cache']):
        return
    files = {k: os.path.join(sdir, 'retinotopy', v % (h, alignment)) for k,
        v in six.iteritems(_retinotopy_cache_tr[htype])}
    for p, fl in six.iteritems(files):
        if p not in props or not overwrite and os.path.exists(fl):
            continue
        p = np.asarray(props[p])
        if np.issubdtype(p.dtype, np.floating):
            p = np.asarray(p, np.float32)
        dr = os.path.split(os.path.abspath(fl))[0]
        if not os.path.isdir(dr):
            os.makedirs(os.path.abspath(dr), 493)
        nyio.save(fl, p)