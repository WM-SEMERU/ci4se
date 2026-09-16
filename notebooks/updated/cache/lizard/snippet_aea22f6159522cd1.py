def parse(cls, root):
    subsection = root.tag.replace(utils.lxmlns('mets'), '', 1)
    if subsection not in cls.ALLOWED_SUBSECTIONS:
        raise exceptions.ParseError(
            'SubSection can only parse elements with tag in %s with METS namespace'
             % (cls.ALLOWED_SUBSECTIONS,))
    section_id = root.get('ID')
    created = root.get('CREATED', '')
    status = root.get('STATUS', '')
    child = root[0]
    if child.tag == utils.lxmlns('mets') + 'mdWrap':
        mdwrap = MDWrap.parse(child)
        obj = cls(subsection, mdwrap, section_id)
    elif child.tag == utils.lxmlns('mets') + 'mdRef':
        mdref = MDRef.parse(child)
        obj = cls(subsection, mdref, section_id)
    else:
        raise exceptions.ParseError('Child of %s must be mdWrap or mdRef' %
            subsection)
    obj.created = created
    obj.status = status
    return obj