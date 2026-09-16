def delete_identity(db, identity_id):
    with db.connect() as session:
        identity = find_identity(session, identity_id)
        if not identity:
            raise NotFoundError(entity=identity_id)
        delete_identity_db(session, identity)