def __system_multiCall(calls, **kwargs):
    if not isinstance(calls, list):
        raise RPCInvalidParams(
            'system.multicall first argument should be a list, {} given.'.
            format(type(calls)))
    handler = kwargs.get(HANDLER_KEY)
    results = []
    for call in calls:
        try:
            result = handler.execute_procedure(call['methodName'], args=
                call.get('params'))
            results.append([result])
        except RPCException as e:
            results.append({'faultCode': e.code, 'faultString': e.message})
        except Exception as e:
            results.append({'faultCode': RPC_INTERNAL_ERROR, 'faultString':
                str(e)})
    return results