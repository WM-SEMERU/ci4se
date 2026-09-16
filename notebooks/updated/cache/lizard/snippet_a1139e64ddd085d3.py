def instance_dir(obj):
    d = dict()
    d.update(obj.__dict__)
    d.update(class_dir(obj.__class__))
    result = sorted(d.keys())
    return result