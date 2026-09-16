def validate_jsonschema_from_file(self, json_string, path_to_schema):
    schema = open(path_to_schema).read()
    load_input_json = self.string_to_json(json_string)
    try:
        load_schema = json.loads(schema)
    except ValueError as e:
        raise JsonValidatorError('Error in schema: {}'.format(e))
    self._validate_json(load_input_json, load_schema)