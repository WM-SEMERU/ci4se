def _update_schema_to_aws_notation(self, schema):
    result = {}
    for k, v in schema.items():
        if k == '$ref':
            v = self._aws_model_ref_from_swagger_ref(v)
        if isinstance(v, dict):
            v = self._update_schema_to_aws_notation(v)
        result[k] = v
    return result