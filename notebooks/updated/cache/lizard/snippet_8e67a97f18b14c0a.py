def check_section_unaligned(self):
    file_alignment = self.pefile_handle.OPTIONAL_HEADER.FileAlignment
    unaligned_sections = []
    for section in self.pefile_handle.sections:
        if section.PointerToRawData % file_alignment:
            unaligned_sections.append(section.Name)
    if unaligned_sections:
        return {'description': 'Unaligned section, tamper indication',
            'severity': 3, 'category': 'MALFORMED', 'attributes':
            unaligned_sections}
    return None