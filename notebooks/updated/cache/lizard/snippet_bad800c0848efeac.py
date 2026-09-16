def _var_uint_field_handler(handler, ctx):
    _, self = yield
    queue = ctx.queue
    value = 0
    while True:
        if len(queue) == 0:
            yield ctx.read_data_transition(1, self)
        octet = queue.read_byte()
        value <<= _VAR_INT_VALUE_BITS
        value |= octet & _VAR_INT_VALUE_MASK
        if octet & _VAR_INT_SIGNAL_MASK:
            break
    yield ctx.immediate_transition(handler(value, ctx))