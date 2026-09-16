def create(cls, resource_id, *, account_id, properties=None, tags=None,
    location=None, auto_add=True, auto_commit=False):
    if cls.get(resource_id):
        raise ResourceException('Resource {} already exists'.format(
            resource_id))
    res = Resource()
    res.resource_id = resource_id
    res.account_id = account_id
    res.location = location
    res.resource_type_id = ResourceType.get(cls.resource_type).resource_type_id
    if properties:
        for name, value in properties.items():
            prop = ResourceProperty()
            prop.resource_id = res.resource_id
            prop.name = name
            prop.value = value.isoformat() if type(value
                ) == datetime else value
            res.properties.append(prop)
            db.session.add(prop)
    if tags:
        for key, value in tags.items():
            if type(value) != str:
                raise ValueError('Invalid object type for tag value: {}'.
                    format(key))
            tag = Tag()
            tag.resource_id = resource_id
            tag.key = key
            tag.value = value
            res.tags.append(tag)
            db.session.add(tag)
    if auto_add:
        db.session.add(res)
        if auto_commit:
            db.session.commit()
        return cls.get(res.resource_id)
    else:
        return cls(res)