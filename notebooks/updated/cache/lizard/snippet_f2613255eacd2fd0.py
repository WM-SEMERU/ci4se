def obj_in_list_always(target_list, obj):
    for item in set(target_list):
        if item is not obj:
            return False
    return True