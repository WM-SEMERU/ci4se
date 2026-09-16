def _EvaluateExpressions(self, frame):
    return [self._FormatExpression(frame, expression) for expression in 
        self._definition.get('expressions') or []]