def get_unique_named_object(root, name):
    a = get_children(lambda x: hasattr(x, 'name') and x.name == name, root)
    assert len(a) == 1
    return a[0]