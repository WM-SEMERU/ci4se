def pop_ctx():
    if getattr(_request_ctx_stack.top, 'fixtures_request_context', False):
        _request_ctx_stack.pop()
    if _app_ctx_stack is not None and getattr(_app_ctx_stack.top,
        'fixtures_app_context', False):
        _app_ctx_stack.pop()