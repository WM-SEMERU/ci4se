def _process_binary_trigger(trigger_value, condition):
    ops = {(0): '>', (1): '<', (2): '>=', (3): '<=', (4): '==', (5): 'always'}
    sources = {(0): 'value', (1): 'count'}
    encoded_source = condition & 1
    encoded_op = condition >> 1
    oper = ops.get(encoded_op, None)
    source = sources.get(encoded_source, None)
    if oper is None:
        raise ArgumentError('Unknown operation in binary trigger',
            condition=condition, operation=encoded_op, known_ops=ops)
    if source is None:
        raise ArgumentError('Unknown value source in binary trigger',
            source=source, known_sources=sources)
    if oper == 'always':
        return TrueTrigger()
    return InputTrigger(source, oper, trigger_value)