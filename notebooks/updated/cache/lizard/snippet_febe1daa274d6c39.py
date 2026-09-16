def rm_empty_indices(*args):
    rm_inds = args[0]
    if not rm_inds:
        return args[1:]
    keep_inds = [i for i in range(len(args[1])) if i not in rm_inds]
    return [[a[i] for i in keep_inds] for a in args[1:]]