def getFingerprintsForExpressions(self, body, sparsity=1.0):
    return self._expressions.resolveBulkExpression(self._retina, body, sparsity
        )