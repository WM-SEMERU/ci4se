def get_context_arguments(self):
    cargs = {}
    for context in self.__context_stack:
        cargs.update(context.context_arguments)
    return cargs