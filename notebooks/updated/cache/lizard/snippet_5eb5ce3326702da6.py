def _load_permissions(campus, calendarid, resp_fragment, permission_list):
    for record in resp_fragment:
        if not _is_valid_email(record['Email']):
            continue
        perm = Permission()
        perm.calendarid = calendarid
        perm.campus = campus
        perm.uwnetid = _extract_uwnetid(record['Email'])
        perm.level = record['Level']
        perm.name = str(record['Name'])
        permission_list.append(perm)