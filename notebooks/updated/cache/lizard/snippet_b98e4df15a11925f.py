def collect_source_model_data(self, branch_id, source_model):
    with self._get_source_model(source_model) as sm:
        xml = sm.read()
    self.tectonic_region_types.update(TRT_REGEX.findall(xml))
    self.source_ids[branch_id].extend(ID_REGEX.findall(xml))
    self.source_types.update(SOURCE_TYPE_REGEX.findall(xml))