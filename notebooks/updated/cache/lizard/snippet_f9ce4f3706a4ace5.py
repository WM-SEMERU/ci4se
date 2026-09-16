def _get_user_groups(session, user_id, filter):
    return session.fetch_items('groups.get', Group.from_json, count=1000,
        user_id=user_id, filter=filter, extended=1, fields=','.join(Group.
        GROUP_FIELDS))