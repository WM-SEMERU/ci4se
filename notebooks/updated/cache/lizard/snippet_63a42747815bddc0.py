def add_child(self, **kwargs):
    if not self.is_leaf():
        if self.node_order_by:
            pos = 'sorted-sibling'
        else:
            pos = 'last-sibling'
        last_child = self.get_last_child()
        last_child._cached_parent_obj = self
        return last_child.add_sibling(pos, **kwargs)
    sql, params = self.__class__._move_right(self.tree_id, self.rgt, False, 2)
    if len(kwargs) == 1 and 'instance' in kwargs:
        newobj = kwargs['instance']
        if newobj.pk:
            raise NodeAlreadySaved(
                'Attempted to add a tree node that is already in the database')
    else:
        newobj = get_result_class(self.__class__)(**kwargs)
    newobj.tree_id = self.tree_id
    newobj.depth = self.depth + 1
    newobj.lft = self.lft + 1
    newobj.rgt = self.lft + 2
    self.rgt += 2
    newobj._cached_parent_obj = self
    cursor = self._get_database_cursor('write')
    cursor.execute(sql, params)
    newobj.save()
    return newobj