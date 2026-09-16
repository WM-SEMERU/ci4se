def set_cache(self, instance=None, translation=None, language=None,
    field_name=None, field_value=None):
    if instance is not None and translation is not None:
        cached_obj = CachedTranslation.from_object(translation)
        instance._linguist_translations[translation.field_name][translation
            .language] = cached_obj
        return cached_obj
    if instance is None:
        instance = self.instance
    cached_obj = self.get_cache(instance, translation=translation,
        field_value=field_value, language=language, field_name=field_name)
    if field_value is None and cached_obj.field_value:
        cached_obj.deleted = True
    if field_value != cached_obj.field_value:
        cached_obj.has_changed = True
        cached_obj.field_value = field_value
    return cached_obj