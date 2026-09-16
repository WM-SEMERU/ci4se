def fromSchedulerConstructorArgs(change_filter=None, branch=NotABranch,
    categories=None):
    if change_filter:
        if branch is not NotABranch or categories is not None:
            raise RuntimeError(
                'cannot specify both change_filter and branch or categories')
        return change_filter
    elif branch is not NotABranch or categories:
        cfargs = {}
        if branch is not NotABranch:
            cfargs['branch'] = branch
        if categories:
            cfargs['category'] = categories
        return ChangeFilter(**cfargs)
    else:
        return None