def list_members(context, request):
    members = context.members()
    return {'users': [{'username': m.identifier, 'userid': m.userid,
        'roles': context.get_member_roles(m.userid), 'links': [rellink(m,
        request)]} for m in members]}