def applyIndex(self, lst, right):
    if len(right) != 1:
        raise exceptions.EvaluationError(
            '%r can only be applied to one argument, got %r' % (self.left,
            self.right))
    right = right[0]
    if isinstance(right, int):
        return lst[right]
    raise exceptions.EvaluationError(
        "Can't apply %r to argument (%r): integer expected, got %r" % (self
        .left, self.right, right))