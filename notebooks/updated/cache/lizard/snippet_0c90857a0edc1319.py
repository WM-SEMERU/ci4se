def get_pipeline_stage(self, pipeline_key, stage_key=None, sort_by=None):
    if not pipeline_key:
        return requests.codes.bad_request, None
    uri = '/'.join([self.api_uri, self.pipelines_suffix, pipeline_key, self
        .stages_suffix])
    if stage_key:
        uri = '/'.join([uri, stage_key])
    if sort_by:
        if sort_by in ['creationTimestamp', 'lastUpdatedTimestamp']:
            uri += self.sort_by_postfix + sort_by
        else:
            return requests.codes.bad_request, {'success': 'False', 'error':
                "sortBy needs to be 'creationTimestamp', or 'lastUpdatedTimestamp'"
                }
    code, data = self._req('get', uri)
    if stage_key:
        data = list(data.values())
    return code, data