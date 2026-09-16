def _MergeIdenticalCaseInsensitive(self, a, b):
    if a.lower() != b.lower():
        raise MergeError(
            "values must be the same (case insensitive) ('%s' vs '%s')" % (
            transitfeed.EncodeUnicode(a), transitfeed.EncodeUnicode(b)))
    return b