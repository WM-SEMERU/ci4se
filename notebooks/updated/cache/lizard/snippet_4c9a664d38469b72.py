def add_person_entity(self, entity, instances_json):
    check_type(instances_json, dict, [entity.plural])
    entity_ids = list(map(str, instances_json.keys()))
    self.persons_plural = entity.plural
    self.entity_ids[self.persons_plural] = entity_ids
    self.entity_counts[self.persons_plural] = len(entity_ids)
    for instance_id, instance_object in instances_json.items():
        check_type(instance_object, dict, [entity.plural, instance_id])
        self.init_variable_values(entity, instance_object, str(instance_id))
    return self.get_ids(entity.plural)