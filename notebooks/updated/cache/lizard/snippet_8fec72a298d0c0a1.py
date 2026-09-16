def is_shape(obj, shape):
    if not hasattr(obj, 'shape') or len(obj.shape) != len(shape):
        return False
    for i, target in zip(obj.shape, shape):
        if is_sequence(target):
            if i in target:
                continue
            else:
                return False
        if target < 0:
            if i == 0:
                return False
            else:
                continue
        if target != i:
            return False
    return True