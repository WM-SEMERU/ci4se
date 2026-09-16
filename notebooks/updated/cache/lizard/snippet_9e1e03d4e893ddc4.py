def _remap_tag_to_tag_id(cls, tag, new_data):
    try:
        value = new_data[tag]
    except:
        return
    tag_id = tag + '_id'
    try:
        new_data[tag_id] = value['id']
    except:
        try:
            new_data[tag_id] = value.id
        except AttributeError:
            new_data[tag_id] = value
    del new_data[tag]