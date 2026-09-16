def _MergeIdentical(self, a, b):
    if a != b:
        raise MergeError("values must be identical ('%s' vs '%s')" % (
            transitfeed.EncodeUnicode(a), transitfeed.EncodeUnicode(b)))
    return b