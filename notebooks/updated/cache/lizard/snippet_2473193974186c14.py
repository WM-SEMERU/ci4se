def catalog_object_id(self, catalog_object_id):
    if catalog_object_id is None:
        raise ValueError(
            'Invalid value for `catalog_object_id`, must not be `None`')
    if len(catalog_object_id) > 192:
        raise ValueError(
            'Invalid value for `catalog_object_id`, length must be less than `192`'
            )
    self._catalog_object_id = catalog_object_id