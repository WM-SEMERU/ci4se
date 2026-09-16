def is_ancestor(self, child_key_name, ancestor_key_name):
    if ancestor_key_name is None:
        return True
    one_up_parent = self.dct[child_key_name]['parent']
    if child_key_name == ancestor_key_name:
        return True
    elif one_up_parent is None:
        return False
    else:
        return self.is_ancestor(one_up_parent, ancestor_key_name)