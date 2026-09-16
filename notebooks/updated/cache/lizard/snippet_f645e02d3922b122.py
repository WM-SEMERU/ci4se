def _constructor(cls, mapping, configuration):
    attr = cls(mapping)
    attr._setattr('_sequence_type', configuration)
    return attr