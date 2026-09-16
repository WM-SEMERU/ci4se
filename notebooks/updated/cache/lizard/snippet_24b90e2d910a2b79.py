def _bson_to_dict(data, opts):
    try:
        if _raw_document_class(opts.document_class):
            return opts.document_class(data, opts)
        _, end = _get_object_size(data, 0, len(data))
        return _elements_to_dict(data, 4, end, opts)
    except InvalidBSON:
        raise
    except Exception:
        _, exc_value, exc_tb = sys.exc_info()
        reraise(InvalidBSON, exc_value, exc_tb)