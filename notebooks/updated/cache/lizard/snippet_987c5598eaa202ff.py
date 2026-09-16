def __up_cmp(self, obj1, obj2):
    if obj1.update_order > obj2.update_order:
        return 1
    elif obj1.update_order < obj2.update_order:
        return -1
    else:
        return 0