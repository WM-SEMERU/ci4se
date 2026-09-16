def create_pipeline_field(self, pipeline_key, name, field_type, **kwargs):
    uri = '/'.join([self.api_uri, self.pipelines_suffix, pipeline_key, self
        .fields_suffix])
    code, data = self._create_field(uri, name, field_type, **kwargs)
    return code, data