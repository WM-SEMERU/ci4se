def check_files(filelist, file_stage_manager=None, return_found=True,
    return_missing=True):
    found = []
    missing = []
    none_count = 0
    for fname in filelist:
        if fname is None:
            none_count += 1
            continue
        if fname[0] == '@':
            fname = fname[1:]
        if os.path.exists(fname):
            found.append(fname)
            continue
        if os.path.exists(fname + '.gz'):
            found.append(fname)
            continue
        if file_stage_manager is not None:
            fname = file_stage_manager.get_scratch_path(fname)
            if os.path.exists(fname):
                found.append(fname)
                continue
        missing.append(fname)
    if return_found and return_missing:
        return found, missing
    elif return_found:
        return found
    elif return_missing:
        return missing
    return None