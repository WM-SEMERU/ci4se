def record_prefix(required_type, factory):
    field = record_type(required_type)
    field += factory.get_rule('transaction_sequence_n')
    field += factory.get_rule('record_sequence_n')
    return field