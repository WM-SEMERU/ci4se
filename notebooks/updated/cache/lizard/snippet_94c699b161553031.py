def delete_pipeline(self, pipeline_key):
    if pipeline_key:
        uri = '/'.join([self.api_uri, self.pipelines_suffix, pipeline_key])
        return self._req('delete', uri)
    else:
        return requests.codes.bad_request, None