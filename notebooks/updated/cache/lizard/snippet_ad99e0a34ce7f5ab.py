def add_institution(self, institution, start_date=None, end_date=None, rank
    =None, record=None, curated=False, current=False):
    new_institution = {}
    new_institution['institution'] = institution
    if start_date:
        new_institution['start_date'] = normalize_date(start_date)
    if end_date:
        new_institution['end_date'] = normalize_date(end_date)
    if rank:
        new_institution['rank'] = rank
    if record:
        new_institution['record'] = record
    new_institution['curated_relation'] = curated
    new_institution['current'] = current
    self._append_to('positions', new_institution)
    self.obj['positions'].sort(key=self._get_institution_priority_tuple,
        reverse=True)