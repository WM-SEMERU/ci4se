def parse(self):
    self.tree = self._build_tree(self.html_contents)
    self.elts_to_keep = self._get_elements_to_keep()
    self.elts_to_discard = self._get_elements_to_discard()
    self.elts_to_remove = []
    is_root = self._is_keep(self.tree)
    has_descendant = self._has_keep_elt_in_descendants(self.tree)
    if not (is_root or has_descendant):
        return False
    self._parse_element(self.tree, parent_is_keep=is_root)
    self._remove_elements(self.elts_to_remove)
    return True