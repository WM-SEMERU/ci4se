def map(cls, obj, mode='data', backend=None):
    from .overlay import CompositeOverlay
    element_compositors = [c for c in cls.definitions if len(c.
        _pattern_spec) == 1]
    overlay_compositors = [c for c in cls.definitions if len(c.
        _pattern_spec) > 1]
    if overlay_compositors:
        obj = obj.map(lambda obj: cls.collapse_element(obj, mode=mode,
            backend=backend), [CompositeOverlay])
    element_patterns = [c.pattern for c in element_compositors]
    if element_compositors and obj.traverse(lambda x: x, element_patterns):
        obj = obj.map(lambda obj: cls.collapse_element(obj, mode=mode,
            backend=backend), element_patterns)
    return obj