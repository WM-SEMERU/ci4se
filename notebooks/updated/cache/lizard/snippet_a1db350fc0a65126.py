def is_dependent_ssa(variable, source, context, only_unprotected=False):
    assert isinstance(context, (Contract, Function))
    context = context.context
    if isinstance(variable, Constant):
        return False
    if variable == source:
        return True
    if only_unprotected:
        return variable in context[KEY_SSA_UNPROTECTED] and source in context[
            KEY_SSA_UNPROTECTED][variable]
    return variable in context[KEY_SSA] and source in context[KEY_SSA][variable
        ]