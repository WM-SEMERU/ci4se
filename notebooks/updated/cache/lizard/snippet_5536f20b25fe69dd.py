def _schema_to_json_file_object(self, schema_list, file_obj):
    json.dump(schema_list, file_obj, indent=2, sort_keys=True)