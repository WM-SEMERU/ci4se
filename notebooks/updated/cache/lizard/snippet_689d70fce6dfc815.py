def get_enabled_references(self, datas, meta_references):
    references = OrderedDict()
    for section in meta_references:
        references[section] = self.get_reference(datas, section)
    return references