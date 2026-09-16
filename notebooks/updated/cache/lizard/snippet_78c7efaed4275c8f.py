def existing_users(context):
    members = IWorkspace(context).members
    info = []
    for userid, details in members.items():
        user = api.user.get(userid)
        if user is None:
            continue
        user = user.getUser()
        title = user.getProperty('fullname') or user.getId() or userid
        description = _('Here we could have a nice status of this person')
        classes = description and 'has-description' or 'has-no-description'
        portal = api.portal.get()
        portrait = '%s/portal_memberdata/portraits/%s' % (portal.
            absolute_url(), userid)
        info.append(dict(id=userid, title=title, description=description,
            portrait=portrait, cls=classes, member=True, admin='Admins' in
            details['groups']))
    return info