def where_unique(cls, ip, object_id, location):
    return cls.query.filter_by(ip=ip, object_id=object_id, location=location
        ).first()