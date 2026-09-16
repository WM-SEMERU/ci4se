def transpose(obj, semitone):
    _check_supported(obj)
    copied = deepcopy(obj)
    copied.transpose(semitone)
    return copied