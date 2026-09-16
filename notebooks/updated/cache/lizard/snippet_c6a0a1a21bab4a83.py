def get_or_create(self, **kwargs):
    with auto_populate(self._populate_mode):
        return super(MultilingualQuerySet, self).get_or_create(**kwargs)