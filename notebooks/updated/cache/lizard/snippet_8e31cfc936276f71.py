def _filter_dicts(self):
    keys_to_remove = set()
    for ref_name in self.report:
        for ctg_name in self.report[ref_name]:
            self.report[ref_name][ctg_name] = self._filter_list_of_dicts(self
                .report[ref_name][ctg_name])
            if len(self.report[ref_name][ctg_name]) == 0:
                keys_to_remove.add((ref_name, ctg_name))
    refs_to_remove = set()
    for ref_name, ctg_name in keys_to_remove:
        del self.report[ref_name][ctg_name]
        if len(self.report[ref_name]) == 0:
            refs_to_remove.add(ref_name)
    for ref_name in refs_to_remove:
        del self.report[ref_name]