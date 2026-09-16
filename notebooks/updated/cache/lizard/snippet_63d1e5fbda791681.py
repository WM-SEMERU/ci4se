def _nested_output(obj):
    nested.__opts__ = __opts__
    ret = nested.output(obj).rstrip()
    return ret