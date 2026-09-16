def check_section_oversized(self):
    total_image_size = self.pefile_handle.OPTIONAL_HEADER.SizeOfImage
    for section in self.pefile_handle.sections:
        if section.PointerToRawData + section.SizeOfRawData > total_image_size:
            return {'description':
                'Oversized section, storing addition data within the PE',
                'severity': 3, 'category': 'MALFORMED', 'attributes':
                section.Name}
    return None