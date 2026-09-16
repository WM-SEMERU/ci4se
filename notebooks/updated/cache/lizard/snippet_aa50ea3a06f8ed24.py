def get(cls, resource_type):
    if isinstance(resource_type, str):
        obj = getattr(db, cls.__name__).find_one(cls.resource_type ==
            resource_type)
    elif isinstance(resource_type, int):
        obj = getattr(db, cls.__name__).find_one(cls.resource_type_id ==
            resource_type)
    elif isinstance(resource_type, cls):
        return resource_type
    else:
        obj = None
    if not obj:
        obj = cls()
        obj.resource_type = resource_type
        db.session.add(obj)
        db.session.commit()
        db.session.refresh(obj)
    return obj