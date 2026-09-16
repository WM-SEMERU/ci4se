def get_study_items(self):
    study_items = set()
    for rec in self.goea_results:
        study_items |= rec.study_items
    return study_items