def dumps(o, encoder=None):
    retval = ''
    if encoder is None:
        encoder = TomlEncoder(o.__class__)
    addtoretval, sections = encoder.dump_sections(o, '')
    retval += addtoretval
    outer_objs = [id(o)]
    while sections:
        section_ids = [id(section) for section in sections]
        for outer_obj in outer_objs:
            if outer_obj in section_ids:
                raise ValueError('Circular reference detected')
        outer_objs += section_ids
        newsections = encoder.get_empty_table()
        for section in sections:
            addtoretval, addtosections = encoder.dump_sections(sections[
                section], section)
            if addtoretval or not addtoretval and not addtosections:
                if retval and retval[-2:] != '\n\n':
                    retval += '\n'
                retval += '[' + section + ']\n'
                if addtoretval:
                    retval += addtoretval
            for s in addtosections:
                newsections[section + '.' + s] = addtosections[s]
        sections = newsections
    return retval