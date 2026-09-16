def check_pending_calls():
    result = True
    for id_, params, lineno in global_.FUNCTION_CALLS:
        result = result and check_call_arguments(lineno, id_, params)
    return result