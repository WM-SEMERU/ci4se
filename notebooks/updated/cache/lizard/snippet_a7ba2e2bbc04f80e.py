def remove_once(gset, elem):
    remove = getattr(gset, 'remove', None)
    if remove is not None:
        remove(elem)
    else:
        del gset[elem]
    return elem