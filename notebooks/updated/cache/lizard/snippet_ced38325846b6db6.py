def get_missing_languages(self, field_name, db_table):
    db_table_fields = self.get_table_fields(db_table)
    for lang_code in AVAILABLE_LANGUAGES:
        if build_localized_fieldname(field_name, lang_code
            ) not in db_table_fields:
            yield lang_code