def form_out(self, _form=None):
    _form = _form or self.object_form
    self.output['forms'] = _form.serialize()
    self._add_meta_props(_form)
    self.output['forms']['grouping'] = _form.Meta.grouping
    self.output['forms']['constraints'] = _form.Meta.constraints
    self._patch_form(self.output['forms'])
    self.set_client_cmd('form')