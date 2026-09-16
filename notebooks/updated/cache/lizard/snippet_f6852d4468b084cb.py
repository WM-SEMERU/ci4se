def get_sonos_favorites(self, start=0, max_items=100):
    message = (
        'The output type of this method will probably change in the future to use SoCo data structures'
        )
    warnings.warn(message, stacklevel=2)
    return self.__get_favorites(SONOS_FAVORITES, start, max_items)