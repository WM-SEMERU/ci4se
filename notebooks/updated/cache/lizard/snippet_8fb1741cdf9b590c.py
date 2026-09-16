def get_or_create_candidate(self, row, party, race):
    person = self.get_or_create_person(row)
    id_components = row['id'].split('-')
    candidate_id = '{0}-{1}'.format(id_components[1], id_components[2])
    defaults = {'party': party, 'incumbent': row.get('incumbent')}
    if person.last_name == 'None of these candidates':
        candidate_id = '{0}-{1}'.format(id_components[0], candidate_id)
    candidate, created = election.Candidate.objects.update_or_create(person
        =person, race=race, ap_candidate_id=candidate_id, defaults=defaults)
    return candidate