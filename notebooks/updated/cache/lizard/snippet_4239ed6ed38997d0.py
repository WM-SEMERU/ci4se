def list_device_names(class_path, name_pattern, **kwargs):
    if not os.path.isdir(class_path):
        return

    def matches(attribute, pattern):
        try:
            with io.FileIO(attribute) as f:
                value = f.read().strip().decode()
        except:
            return False
        if isinstance(pattern, list):
            return any([(value.find(p) >= 0) for p in pattern])
        else:
            return value.find(pattern) >= 0
    for f in os.listdir(class_path):
        if fnmatch.fnmatch(f, name_pattern):
            path = class_path + '/' + f
            if all([matches(path + '/' + k, kwargs[k]) for k in kwargs]):
                yield f