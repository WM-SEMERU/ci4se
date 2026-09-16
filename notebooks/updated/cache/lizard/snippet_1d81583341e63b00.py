def save_metadata(self):
    metadata = self.field_mapping_widget.get_field_mapping()
    for key, value in list(metadata['fields'].items()):
        if key in self.metadata['inasafe_default_values']:
            self.metadata['inasafe_default_values'].pop(key)
        if value is None or value == []:
            if key in self.metadata['inasafe_fields']:
                self.metadata['inasafe_fields'].pop(key)
        else:
            self.metadata['inasafe_fields'][key] = value
    for key, value in list(metadata['values'].items()):
        if key in self.metadata['inasafe_fields']:
            self.metadata['inasafe_fields'].pop(key)
        if value is None:
            if key in self.metadata['inasafe_default_values']:
                self.metadata['inasafe_default_values'].pop(key)
        else:
            self.metadata['inasafe_default_values'][key] = value
    try:
        self.keyword_io.write_keywords(layer=self.layer, keywords=self.metadata
            )
    except InaSAFEError as e:
        error_message = get_error_message(e)
        QMessageBox.warning(self, self.tr('InaSAFE'), self.tr(
            """An error was encountered when saving the following keywords:
 %s"""
            ) % error_message.to_html())
    if self.metadata.get('inasafe_default_values'):
        for key, value in list(self.metadata['inasafe_default_values'].items()
            ):
            set_inasafe_default_value_qsetting(self.setting, key, RECENT, value
                )