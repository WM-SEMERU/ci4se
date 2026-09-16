def create_section(self, name, overwrite=True):
    if overwrite:
        sect = ManifestSection(name)
        self.sub_sections[name] = sect
    else:
        sect = self.sub_sections.get(name, None)
        if sect is None:
            sect = ManifestSection(name)
            self.sub_sections[name] = sect
    return sect