def first_or_initialize(cls, parent=None, **attributes):
    existing_resource = cls.find_by(parent, **attributes)
    if existing_resource:
        return existing_resource
    return cls(**attributes)