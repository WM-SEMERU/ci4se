def from_json(cls, data, result=None):
    if data.get('type') != cls._type_value:
        raise exception.ElementDataWrongType(type_expected=cls._type_value,
            type_provided=data.get('type'))
    ref = data.get('ref')
    role = data.get('role')
    attributes = {}
    ignore = ['geometry', 'type', 'ref', 'role']
    for n, v in data.items():
        if n in ignore:
            continue
        attributes[n] = v
    geometry = data.get('geometry')
    if isinstance(geometry, list):
        geometry_orig = geometry
        geometry = []
        for v in geometry_orig:
            geometry.append(RelationWayGeometryValue(lat=v.get('lat'), lon=
                v.get('lon')))
    else:
        geometry = None
    return cls(attributes=attributes, geometry=geometry, ref=ref, role=role,
        result=result)