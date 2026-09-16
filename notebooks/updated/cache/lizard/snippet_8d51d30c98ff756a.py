def igetattr(self, name, context=None, class_context=True):
    context = contextmod.copy_context(context)
    context.lookupname = name
    try:
        attr = self.getattr(name, context, class_context=class_context)[0]
        for inferred in bases._infer_stmts([attr], context, frame=self):
            if not isinstance(inferred, node_classes.Const) and isinstance(
                inferred, bases.Instance):
                try:
                    inferred._proxied.getattr('__get__', context)
                except exceptions.AttributeInferenceError:
                    yield inferred
                else:
                    yield util.Uninferable
            else:
                yield function_to_method(inferred, self)
    except exceptions.AttributeInferenceError as error:
        if not name.startswith('__') and self.has_dynamic_getattr(context):
            yield util.Uninferable
        else:
            raise exceptions.InferenceError(error.message, target=self,
                attribute=name, context=context)