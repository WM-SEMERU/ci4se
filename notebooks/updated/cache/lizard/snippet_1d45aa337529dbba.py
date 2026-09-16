def infer_subscript(self, context=None):
    found_one = False
    for value in self.value.infer(context):
        if value is util.Uninferable:
            yield util.Uninferable
            return None
        for index in self.slice.infer(context):
            if index is util.Uninferable:
                yield util.Uninferable
                return None
            index_value = _SUBSCRIPT_SENTINEL
            if value.__class__ == bases.Instance:
                index_value = index
            elif index.__class__ == bases.Instance:
                instance_as_index = helpers.class_instance_as_index(index)
                if instance_as_index:
                    index_value = instance_as_index
            else:
                index_value = index
            if index_value is _SUBSCRIPT_SENTINEL:
                raise exceptions.InferenceError(node=self, context=context)
            try:
                assigned = value.getitem(index_value, context)
            except (exceptions.AstroidTypeError, exceptions.
                AstroidIndexError, exceptions.AttributeInferenceError,
                AttributeError) as exc:
                raise exceptions.InferenceError(node=self, context=context
                    ) from exc
            if self is assigned or assigned is util.Uninferable:
                yield util.Uninferable
                return None
            yield from assigned.infer(context)
            found_one = True
    if found_one:
        return dict(node=self, context=context)
    return None