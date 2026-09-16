def get(cls, community_id, record_uuid):
    return cls.query.filter_by(id_record=record_uuid, id_community=community_id
        ).one_or_none()