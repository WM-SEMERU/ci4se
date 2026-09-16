def _init_forms(self):
    super(BaseCRUDView, self)._init_forms()
    conv = GeneralModelConverter(self.datamodel)
    if not self.add_form:
        self.add_form = conv.create_form(self.label_columns, self.
            add_columns, self.description_columns, self.validators_columns,
            self.add_form_extra_fields, self.add_form_query_rel_fields)
    if not self.edit_form:
        self.edit_form = conv.create_form(self.label_columns, self.
            edit_columns, self.description_columns, self.validators_columns,
            self.edit_form_extra_fields, self.edit_form_query_rel_fields)