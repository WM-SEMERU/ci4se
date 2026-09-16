def _has_keep_elt_in_descendants(self, elt):
    for d in elt.iterdescendants():
        if d in self.elts_to_keep:
            return True
    return False