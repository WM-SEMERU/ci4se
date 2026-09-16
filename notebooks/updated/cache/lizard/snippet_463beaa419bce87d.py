def add_root(cls, **kwargs):
    last_root = cls.get_last_root_node()
    if last_root and last_root.node_order_by:
        return last_root.add_sibling('sorted-sibling', **kwargs)
    if last_root:
        newtree_id = last_root.tree_id + 1
    else:
        newtree_id = 1
    if len(kwargs) == 1 and 'instance' in kwargs:
        newobj = kwargs['instance']
        if newobj.pk:
            raise NodeAlreadySaved(
                'Attempted to add a tree node that is already in the database')
    else:
        newobj = get_result_class(cls)(**kwargs)
    newobj.depth = 1
    newobj.tree_id = newtree_id
    newobj.lft = 1
    newobj.rgt = 2
    newobj.save()
    return newobj