def search_in_dirs(fname, search_dpaths=[], shortcircuit=True, return_tried
    =False, strict=False):
    fpath_list = []
    tried_list = []
    for dpath in search_dpaths:
        fpath = join(dpath, fname)
        if return_tried:
            tried_list.append(fpath)
        if exists(fpath):
            if shortcircuit:
                if return_tried:
                    return fpath, tried_list
                return fpath
            else:
                fpath_list.append(fpath)
    if strict and len(fpath_list) == 0:
        msg = 'Cannot find: fname=%r\n' % (fname,)
        if return_tried:
            msg += 'Tried: \n    ' + '\n    '.join(tried_list)
        raise Exception(msg)
    if shortcircuit:
        if return_tried:
            return None, tried_list
        return None
    else:
        if return_tried:
            return fpath_list, tried_list
        return fpath_list