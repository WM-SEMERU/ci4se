def get_proficiencies_for_resource_on_date(self, resource_id, from_, to):
    proficiency_list = []
    for proficiency in self.get_proficiencies_for_resource(resource_id):
        if overlap(from_, to, proficiency.start_date, proficiency.end_date):
            proficiency_list.append(proficiency)
    return objects.ProficiencyList(proficiency_list, runtime=self._runtime)