def validate(self, strict=True):
    result = self._validate()
    if strict and len(result):
        for r in result:
            logger.error(r)
        raise errs.ValidationError('this Swagger App contains error: {0}.'.
            format(len(result)))
    return result