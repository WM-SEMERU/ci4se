def _make_order(field_path, direction):
    return query_pb2.StructuredQuery.Order(field=query_pb2.StructuredQuery.
        FieldReference(field_path=field_path), direction=
        _enum_from_direction(direction))