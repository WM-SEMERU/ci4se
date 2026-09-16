def clear(self):
    for sub in self.sub_sections.values():
        sub.clear()
    self.sub_sections.clear()
    ManifestSection.clear(self)