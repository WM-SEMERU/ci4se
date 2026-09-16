def get_current_m2m_diff(self, instance, new_objects):
    new_ids = self.pks_from_objects(new_objects)
    relation_manager = self.__get__(instance)
    filter = Q(**{relation_manager.source_field.attname: instance.pk})
    qs = self.through.objects.current.filter(filter)
    try:
        target_name = relation_manager.target_field.attname
    except AttributeError:
        target_name = relation_manager.through._meta.get_field_by_name(
            relation_manager.target_field_name)[0].attname
    current_ids = set(qs.values_list(target_name, flat=True))
    being_removed = current_ids - new_ids
    being_added = new_ids - current_ids
    return list(being_removed), list(being_added)