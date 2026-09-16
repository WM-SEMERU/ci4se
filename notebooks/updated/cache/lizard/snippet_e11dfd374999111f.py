def remove_organisation_from_all(cls, organisation_id):
    users = yield views.organisation_members.get(key=organisation_id,
        include_docs=True)
    users = [x['doc'] for x in users['rows']]
    for user in users:
        user['organisations'][organisation_id]['state'
            ] = State.deactivated.name
    db = cls.db_client()
    yield db.save_docs(users)