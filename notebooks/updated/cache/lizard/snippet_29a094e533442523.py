def _write_source_code(tlobject, kind, builder, type_constructors):
    _write_class_init(tlobject, kind, type_constructors, builder)
    _write_resolve(tlobject, builder)
    _write_to_dict(tlobject, builder)
    _write_to_bytes(tlobject, builder)
    _write_from_reader(tlobject, builder)
    _write_read_result(tlobject, builder)