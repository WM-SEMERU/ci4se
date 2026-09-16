def ensure_context(**vars):
    ctx = _context_stack.top
    stacked = False
    if not ctx:
        ctx = Context()
        stacked = True
        _context_stack.push(ctx)
    ctx.update(vars)
    try:
        yield ctx
    finally:
        if stacked:
            _context_stack.pop()