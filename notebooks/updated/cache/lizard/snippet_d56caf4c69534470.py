def v1_tag_associate(request, tags, tag):
    tag = tag.decode('utf-8').strip()
    assoc = dict(json.loads(request.body.read()), **{'tag': tag})
    tags.add(assoc)