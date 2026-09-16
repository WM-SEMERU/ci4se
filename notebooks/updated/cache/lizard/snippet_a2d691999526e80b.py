def _departmentsVoc(self):
    query = {'portal_type': 'Department', 'is_active': True}
    results = api.search(query, 'bika_setup_catalog')
    items = map(lambda dept: (api.get_uid(dept), api.get_title(dept)), results)
    dept_uids = map(api.get_uid, results)
    depts = self.getDepartments()
    for dept in depts:
        uid = api.get_uid(dept)
        if uid in dept_uids:
            continue
        items.append((uid, api.get_title(dept)))
    return api.to_display_list(items, sort_by='value', allow_empty=False)