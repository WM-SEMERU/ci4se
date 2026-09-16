def bool_value(self):
    context = contextmod.InferenceContext()
    context.callcontext = contextmod.CallContext(args=[])
    context.boundnode = self
    try:
        result = _infer_method_result_truth(self, BOOL_SPECIAL_METHOD, context)
    except (exceptions.InferenceError, exceptions.AttributeInferenceError):
        try:
            result = _infer_method_result_truth(self, '__len__', context)
        except (exceptions.AttributeInferenceError, exceptions.InferenceError):
            return True
    return result