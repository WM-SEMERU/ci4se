def to_dict(item):

    def convert(item):
        if isinstance(item, IterableObject):
            if isinstance(item.source, dict):
                return {k: (convert(v.source) if hasattr(v, 'source') else
                    convert(v)) for k, v in item}
            else:
                return convert(item.source)
        elif isinstance(item, dict):
            return {k: convert(v) for k, v in item.items()}
        elif isinstance(item, list):

            def yield_convert(item):
                for index, value in enumerate(item):
                    yield convert(value)
            return list(yield_convert(item))
        else:
            return item
    return convert(item)