def get_snapshot_count(obj):
    try:
        annotation = IAnnotations(obj)
    except TypeError:
        return 0
    storage = annotation.get(SNAPSHOT_STORAGE, [])
    return len(storage)