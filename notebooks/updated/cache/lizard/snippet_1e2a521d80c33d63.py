def set_filters(self, can_filers=None):
    if self.__set_filters_has_been_called:
        logger.warn(
            'using filters is not supported like this, see note on NicanBus')
    else:
        self.__set_filters_has_been_called = True