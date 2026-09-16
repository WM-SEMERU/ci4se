def _update_attribute_details(self, **update_props):
    tree_to_update = update_props['tree_to_update']
    xpath = self._data_map['_attr_citation']
    self._attr_details_file_url = None
    remove_element(tree_to_update, xpath, True)
    return self._update_complex_list(**update_props)