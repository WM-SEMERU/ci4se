def is_base_dir(d):
    if not dir_param_valid(d):
        raise
    else:
        mfn = os.path.join(d, 's2')
        return os.path.isdir(mfn)