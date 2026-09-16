def save(self, inplace=True):
    modified_data = self._modified_data()
    if bool(modified_data):
        extra = {'resource': self.__class__.__name__, 'query': {'id': self.
            id, 'modified_data': modified_data}}
        logger.info('Saving marker', extra=extra)
        data = self._api.patch(url=self._URL['get'].format(id=self.id),
            data=modified_data).json()
        marker = Marker(api=self._api, **data)
        return marker
    else:
        raise ResourceNotModified()