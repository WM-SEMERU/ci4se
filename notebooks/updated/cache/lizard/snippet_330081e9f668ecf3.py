def _GetSectionNames(self, pefile_object):
    section_names = []
    for section in pefile_object.sections:
        section_name = getattr(section, 'Name', b'')
        try:
            section_name = '{0:s}'.format(section_name.decode('unicode_escape')
                )
        except UnicodeDecodeError:
            section_name = '{0:s}'.format(repr(section_name))
        section_names.append(section_name)
    return section_names