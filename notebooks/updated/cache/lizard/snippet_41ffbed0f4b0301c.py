def _discover_cover_image(zf, opf_xmldoc, opf_filepath):
    content = None
    filepath = None
    extension = None
    tag = find_tag(opf_xmldoc, 'meta', 'name', 'cover')
    if tag and 'content' in tag.attributes.keys():
        item_id = tag.attributes['content'].value
        if item_id:
            filepath, extension = find_img_tag(opf_xmldoc, 'item', 'id',
                item_id)
    if not filepath:
        filepath, extension = find_img_tag(opf_xmldoc, 'item', 'id',
            'cover-image')
    if not filepath:
        filepath, extension = find_img_tag(opf_xmldoc, 'item', 'id', 'cover')
    if filepath:
        base_dir = os.path.dirname(opf_filepath)
        coverpath = os.path.normpath(os.path.join(base_dir, filepath))
        content = zf.read(coverpath)
        content = base64.b64encode(content)
    return content, extension