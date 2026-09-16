def parse(cls, root):
    if root.tag != utils.lxmlns('mets') + 'amdSec':
        raise exceptions.ParseError(
            'AMDSec can only parse amdSec elements with METS namespace.')
    section_id = root.get('ID')
    subsections = []
    for child in root:
        subsection = SubSection.parse(child)
        subsections.append(subsection)
    return cls(section_id, subsections)