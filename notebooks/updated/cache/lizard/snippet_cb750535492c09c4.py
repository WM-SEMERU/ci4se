def to_madeline(self):
    madeline_header = ['FamilyID', 'IndividualID', 'Gender', 'Father',
        'Mother', 'Affected', 'Proband', 'Consultand', 'Alive']
    yield '\t'.join(madeline_header)
    for family_id in self.families:
        for individual_id in self.families[family_id].individuals:
            individual = self.families[family_id].individuals[individual_id]
            yield individual.to_madeline()