def _get_span_name(servicer_context):
    method_name = servicer_context._rpc_event.call_details.method[1:]
    if isinstance(method_name, bytes):
        method_name = method_name.decode('utf-8')
    method_name = method_name.replace('/', '.')
    return '{}.{}'.format(RECV_PREFIX, method_name)