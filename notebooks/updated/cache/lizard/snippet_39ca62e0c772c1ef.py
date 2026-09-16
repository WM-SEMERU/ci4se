def compile_dm_users(self):
    dm_data = self._read_from_json('dms.json')
    dms = dm_data.values()
    all_dms_users = []
    for dm in dms:
        if dm['id'] not in self._EMPTY_DMS:
            try:
                dm_members = {'id': dm['id'], 'users': [self.__USER_DATA[m] for
                    m in dm['members']]}
                all_dms_users.append(dm_members)
            except KeyError:
                dm_members = None
    return all_dms_users