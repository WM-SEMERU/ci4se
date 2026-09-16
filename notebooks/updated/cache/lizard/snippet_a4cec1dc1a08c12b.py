def _add_study(self, study):
    str = '{study} {name}({period})' if study['params'].get('str', None
        ) == None else study['params']['str']
    study['params']['str'] = str
    if not study['name']:
        study['name'] = ta.get_column_name(study['kind'].upper(), study=
            study['kind'], str=str, period=study['params'].get('periods',
            None), column=study['params'].get('column', None))
    restore = study['display'].pop('restore', False)
    if restore:
        _ = self.studies.pop(study['kind'], None)
    if study['kind'] in self.studies:
        try:
            id = '{0} ({1})'.format(study['kind'], study['params']['periods'])
        except:
            id = '{0} ({1})'.format(study['kind'], '(2)')
    else:
        id = study['kind']
    _id = id
    n = 1
    while id in self.studies:
        id = '{0} ({1})'.format(_id, n)
        n += 1
    self.studies[id] = study