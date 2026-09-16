def macro_def(self, macro_ref, frame):
    arg_tuple = ', '.join(repr(x.name) for x in macro_ref.node.args)
    name = getattr(macro_ref.node, 'name', None)
    if len(macro_ref.node.args) == 1:
        arg_tuple += ','
    self.write(
        'Macro(environment, macro, %r, (%s), %r, %r, %r, context.eval_ctx.autoescape)'
         % (name, arg_tuple, macro_ref.accesses_kwargs, macro_ref.
        accesses_varargs, macro_ref.accesses_caller))