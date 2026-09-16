def get_value(self, context):
    if self.value:
        return expressions.eval_string(self.value, context)
    else:
        raise ValueError(
            '!py string expression is empty. It must be a valid python expression instead.'
            )