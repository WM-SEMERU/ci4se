def get_section_by_rva(self, rva):
    sections = [s for s in self.sections if s.contains_rva(rva)]
    if sections:
        return sections[0]
    return None