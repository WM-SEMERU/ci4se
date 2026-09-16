def check(self, val):
    if self.type is None:
        return True
    is_list = isinstance(val, list)
    if not self.listable and is_list:
        return False
    if self.type == KEY_TYPES.NUMERIC and not is_number(val):
        return False
    elif self.type == KEY_TYPES.TIME and not is_number(val
        ) and '-' not in val and '/' not in val:
        return False
    elif self.type == KEY_TYPES.STRING:
        if is_list:
            if not isinstance(val[0], basestring):
                return False
        elif not isinstance(val, basestring):
            return False
    elif self.type == KEY_TYPES.BOOL:
        if is_list and not isinstance(val[0], bool):
            return False
        elif not isinstance(val, bool):
            return False
    return True