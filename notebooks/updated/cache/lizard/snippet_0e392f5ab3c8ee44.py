def make_section(section_id=None, contents=None):
    section = nodes.section()
    section['ids'].append(nodes.make_id(section_id))
    section['names'].append(section_id)
    if contents is not None:
        section.extend(contents)
    return section