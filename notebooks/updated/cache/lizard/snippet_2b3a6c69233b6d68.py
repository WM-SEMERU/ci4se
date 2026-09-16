def get_modification_date(brain_or_object):
    modified = getattr(brain_or_object, 'modified', None)
    if modified is None:
        fail('Object {} has no modification date '.format(repr(
            brain_or_object)))
    if callable(modified):
        return modified()
    return modified