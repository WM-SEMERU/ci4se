def _Execute(statements, context, callback, trace):
    if trace:
        trace.exec_depth += 1
    for i, statement in enumerate(statements):
        if isinstance(statement, six.string_types):
            callback(statement)
        else:
            try:
                func, args = statement
                func(args, context, callback, trace)
            except UndefinedVariable as e:
                start = max(0, i - 3)
                end = i + 3
                e.near = statements[start:end]
                e.trace = trace
                raise