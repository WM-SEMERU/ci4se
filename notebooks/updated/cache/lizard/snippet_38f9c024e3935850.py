def _convert_attribute_to_tag(key, attr):
    if isinstance(attr, bool):
        return jaeger.Tag(key=key, vBool=attr, vType=jaeger.TagType.BOOL)
    if isinstance(attr, str):
        return jaeger.Tag(key=key, vStr=attr, vType=jaeger.TagType.STRING)
    if isinstance(attr, int):
        return jaeger.Tag(key=key, vLong=attr, vType=jaeger.TagType.LONG)
    if isinstance(attr, float):
        return jaeger.Tag(key=key, vDouble=attr, vType=jaeger.TagType.DOUBLE)
    logging.warn('Could not serialize attribute             {}:{} to tag'.
        format(key, attr))
    return None