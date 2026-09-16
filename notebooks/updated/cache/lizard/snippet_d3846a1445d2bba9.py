def delete_from_matching_blacklist(db, entity):
    with db.connect() as session:
        mb = session.query(MatchingBlacklist).filter(MatchingBlacklist.
            excluded == entity).first()
        if not mb:
            raise NotFoundError(entity=entity)
        delete_from_matching_blacklist_db(session, mb)