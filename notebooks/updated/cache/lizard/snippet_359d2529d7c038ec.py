def verify_directory(verbose=True, max_size_mb=50):
    ok = True
    mb_to_bytes = 1000 * 1000
    expected_files = ['config.txt', 'experiment.py']
    for f in expected_files:
        if os.path.exists(f):
            log('✓ {} is PRESENT'.format(f), chevrons=False, verbose=verbose)
        else:
            log('✗ {} is MISSING'.format(f), chevrons=False, verbose=verbose)
            ok = False
    max_size = max_size_mb * mb_to_bytes
    size = size_on_copy()
    if size > max_size:
        size_in_mb = round(size / mb_to_bytes)
        log('✗ {}MB is TOO BIG (greater than {}MB)'.format(size_in_mb,
            max_size_mb), chevrons=False, verbose=verbose)
        ok = False
    return ok