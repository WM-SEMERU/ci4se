def get_movielens(variant='20m'):
    filename = 'movielens_%s.hdf5' % variant
    path = os.path.join(_download.LOCAL_CACHE_DIR, filename)
    if not os.path.isfile(path):
        log.info("Downloading dataset to '%s'", path)
        _download.download_file(URL_BASE + filename, path)
    else:
        log.info("Using cached dataset at '%s'", path)
    with h5py.File(path, 'r') as f:
        m = f.get('movie_user_ratings')
        plays = csr_matrix((m.get('data'), m.get('indices'), m.get('indptr')))
        return np.array(f['movie']), plays