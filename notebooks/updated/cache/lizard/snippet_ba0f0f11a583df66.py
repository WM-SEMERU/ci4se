def from_xml(cls, child, result=None):
    if child.tag.lower() != cls._type_value:
        raise exception.ElementDataWrongType(type_expected=cls._type_value,
            type_provided=child.tag.lower())
    tags = {}
    node_ids = []
    center_lat = None
    center_lon = None
    for sub_child in child:
        if sub_child.tag.lower() == 'tag':
            name = sub_child.attrib.get('k')
            if name is None:
                raise ValueError('Tag without name/key.')
            value = sub_child.attrib.get('v')
            tags[name] = value
        if sub_child.tag.lower() == 'nd':
            ref_id = sub_child.attrib.get('ref')
            if ref_id is None:
                raise ValueError('Unable to find required ref value.')
            ref_id = int(ref_id)
            node_ids.append(ref_id)
        if sub_child.tag.lower() == 'center':
            center_lat, center_lon = cls.get_center_from_xml_dom(sub_child=
                sub_child)
    way_id = child.attrib.get('id')
    if way_id is not None:
        way_id = int(way_id)
    attributes = {}
    ignore = ['id']
    for n, v in child.attrib.items():
        if n in ignore:
            continue
        attributes[n] = v
    return cls(way_id=way_id, center_lat=center_lat, center_lon=center_lon,
        attributes=attributes, node_ids=node_ids, tags=tags, result=result)