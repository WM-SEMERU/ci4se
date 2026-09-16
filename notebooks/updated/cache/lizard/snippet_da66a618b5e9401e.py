def _set_foreign_attributes_for_create(self, model):
    model.set_attribute(self.get_plain_foreign_key(), self.get_parent_key())
    model.set_attribute(self.get_plain_morph_type(), self._morph_class)