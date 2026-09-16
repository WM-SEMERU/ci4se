def igetattr(self, name, context=None):
    if not context:
        context = contextmod.InferenceContext()
    try:
        if context.push((self._proxied, name)):
            raise exceptions.InferenceError(message=
                'Cannot infer the same attribute again', node=self, context
                =context)
        get_attr = self.getattr(name, context, lookupclass=False)
        yield from _infer_stmts(self._wrap_attr(get_attr, context), context,
            frame=self)
    except exceptions.AttributeInferenceError as error:
        try:
            if self._proxied.__class__.__name__ != 'ClassDef':
                raise exceptions.InferenceError(**vars(error)) from error
            attrs = self._proxied.igetattr(name, context, class_context=False)
            yield from self._wrap_attr(attrs, context)
        except exceptions.AttributeInferenceError as error:
            raise exceptions.InferenceError(**vars(error)) from error