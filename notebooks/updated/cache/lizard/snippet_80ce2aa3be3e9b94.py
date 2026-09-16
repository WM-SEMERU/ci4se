def class_name_str(obj, skip_parent=False):
    rt = str(type(obj)).split(' ')[1][1:-2]
    if skip_parent:
        rt = rt.split('.')[-1]
    return rt