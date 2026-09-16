def _set_cell(self, column_family_id, column, value, timestamp=None, state=None
    ):
    column = _to_bytes(column)
    if isinstance(value, six.integer_types):
        value = _PACK_I64(value)
    value = _to_bytes(value)
    if timestamp is None:
        timestamp_micros = -1
    else:
        timestamp_micros = _microseconds_from_datetime(timestamp)
        timestamp_micros -= timestamp_micros % 1000
    mutation_val = data_v2_pb2.Mutation.SetCell(family_name=
        column_family_id, column_qualifier=column, timestamp_micros=
        timestamp_micros, value=value)
    mutation_pb = data_v2_pb2.Mutation(set_cell=mutation_val)
    self._get_mutations(state).append(mutation_pb)