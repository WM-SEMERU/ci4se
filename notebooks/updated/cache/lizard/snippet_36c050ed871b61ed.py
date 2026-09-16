def jinja_block_as_fragment_extension(name, tagname=None, classname=None):
    if tagname is None:
        tagname = name
    if classname is None:
        classname = '%sBlockFragmentExtension' % name.capitalize()
    return type(classname, (BaseJinjaBlockAsFragmentExtension,), {'tags':
        set([tagname]), 'end_tag': 'end' + tagname, 'block_name': name})