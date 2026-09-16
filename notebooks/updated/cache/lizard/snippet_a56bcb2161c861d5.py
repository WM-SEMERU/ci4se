def get_attributes(self):
    items = {}
    items['form_method'] = self.form_method.strip()
    items['form_tag'] = self.form_tag
    items['form_style'] = self.form_style.strip()
    if self.form_action:
        items['form_action'] = self.form_action.strip()
    if self.form_id:
        items['id'] = self.form_id.strip()
    if self.form_class:
        items['class'] = self.form_class.strip()
    if self.inputs:
        items['inputs'] = self.inputs
    if self.form_error_title:
        items['form_error_title'] = self.form_error_title.strip()
    if self.formset_error_title:
        items['formset_error_title'] = self.formset_error_title.strip()
    return items