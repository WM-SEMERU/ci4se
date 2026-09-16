def pageId(self):
    if self.mets is None:
        raise Exception(
            "OcrdFile %s has no member 'mets' pointing to parent OcrdMets" %
            self)
    return self.mets.get_physical_page_for_file(self)