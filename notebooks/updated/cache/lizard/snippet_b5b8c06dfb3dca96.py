def _convert_internal(cls, record):
    if isinstance(record, list):
        return [cls._convert(r) for r in record]
    else:
        return cls._convert(record)