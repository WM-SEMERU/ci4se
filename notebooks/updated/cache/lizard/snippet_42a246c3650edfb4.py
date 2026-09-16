def _infer_stmts(stmts, context, frame=None):
    inferred = False
    if context is not None:
        name = context.lookupname
        context = context.clone()
    else:
        name = None
        context = contextmod.InferenceContext()
    for stmt in stmts:
        if stmt is util.Uninferable:
            yield stmt
            inferred = True
            continue
        context.lookupname = stmt._infer_name(frame, name)
        try:
            for inferred in stmt.infer(context=context):
                yield inferred
                inferred = True
        except exceptions.NameInferenceError:
            continue
        except exceptions.InferenceError:
            yield util.Uninferable
            inferred = True
    if not inferred:
        raise exceptions.InferenceError(
            'Inference failed for all members of {stmts!r}.', stmts=stmts,
            frame=frame, context=context)