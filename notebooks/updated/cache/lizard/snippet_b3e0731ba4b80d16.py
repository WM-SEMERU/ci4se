def set_value(self, comp_str, comp_att):
    super(CPEComponent1_1, self).set_value(comp_str, comp_att)
    self._is_negated = comp_str.startswith('~')