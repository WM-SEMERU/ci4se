def create(cls, community, record, user=None, expires_at=None, notify=True):
    if expires_at and expires_at < datetime.utcnow():
        raise InclusionRequestExpiryTimeError(community=community, record=
            record)
    if community.has_record(record):
        raise InclusionRequestObsoleteError(community=community, record=record)
    try:
        with db.session.begin_nested():
            obj = cls(id_community=community.id, id_record=record.id, user=
                user, expires_at=expires_at)
            db.session.add(obj)
    except (IntegrityError, FlushError):
        raise InclusionRequestExistsError(community=community, record=record)
    inclusion_request_created.send(current_app._get_current_object(),
        request=obj, notify=notify)
    return obj