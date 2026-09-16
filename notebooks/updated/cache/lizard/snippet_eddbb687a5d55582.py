def cli(env, identifier, name, note, tag):
    image_mgr = SoftLayer.ImageManager(env.client)
    data = {}
    if name:
        data['name'] = name
    if note:
        data['note'] = note
    if tag:
        data['tag'] = tag
    image_id = helpers.resolve_id(image_mgr.resolve_ids, identifier, 'image')
    if not image_mgr.edit(image_id, **data):
        raise exceptions.CLIAbort('Failed to Edit Image')