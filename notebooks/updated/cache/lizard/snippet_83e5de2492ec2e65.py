def are_equal(self, sp1, sp2):
    set1 = set(sp1.element_composition.values())
    set2 = set(sp2.element_composition.values())
    if set1 == set2:
        return True
    else:
        return False