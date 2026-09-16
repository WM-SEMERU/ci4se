def cut_sequences_relative(records, slices, record_id):
    with _record_buffer(records) as r:
        try:
            record = next(i for i in r() if i.id == record_id)
        except StopIteration:
            raise ValueError('Record with id {0} not found.'.format(record_id))
        new_slices = _update_slices(record, slices)
        for record in multi_cut_sequences(r(), new_slices):
            yield record