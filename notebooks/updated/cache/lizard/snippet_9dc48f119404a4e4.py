def rescale(self, factor=1.0, allow_cast=True):
    try:
        self.y /= factor
    except TypeError as e:
        logger.warning('Division in place is impossible: %s', e)
        if allow_cast:
            self.y = self.y / factor
        else:
            logger.error('allow_cast flag set to True should help')
            raise