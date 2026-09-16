def evaluate_inline(self, expression, context=None, escape=None,
    safe_wrapper=None):
    if context is None:
        context = {}
    try:
        with self._evaluation_context(escape, safe_wrapper):
            compiled = self._environment.compile_expression(expression)
            return compiled(**context)
    except jinja2.TemplateError as error:
        raise EvaluationError(error.args[0])