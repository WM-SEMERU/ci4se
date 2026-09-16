def infer_unaryop(self, context=None):
    yield from _filter_operation_errors(self, _infer_unaryop, context, util
        .BadUnaryOperationMessage)
    return dict(node=self, context=context)