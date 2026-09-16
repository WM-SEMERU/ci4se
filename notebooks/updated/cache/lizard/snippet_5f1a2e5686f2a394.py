def define_both_methods(class_name, class_dict, old_name, new_name):
    assert old_name not in class_dict or new_name not in class_dict, 'Class "{}" cannot define both "{}" and "{}" methods.'.format(
        class_name, old_name, new_name)
    if old_name in class_dict:
        class_dict[new_name] = class_dict[old_name]
    elif new_name in class_dict:
        class_dict[old_name] = class_dict[new_name]