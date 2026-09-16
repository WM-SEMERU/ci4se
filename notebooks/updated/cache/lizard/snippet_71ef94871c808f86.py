def get_member_ids():
    pm = get_tool('portal_membership')
    member_ids = pm.listMemberIds()
    return filter(lambda x: x, member_ids)