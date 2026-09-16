def create_insight(self, project_key, **kwargs):
    request = self.__build_insight_obj(lambda : _swagger.
        InsightCreateRequest(title=kwargs.get('title'), body=_swagger.
        InsightBody(image_url=kwargs.get('image_url'), embed_url=kwargs.get
        ('embed_url'), markdown_body=kwargs.get('markdown_body'))), kwargs)
    project_owner, project_id = parse_dataset_key(project_key)
    try:
        _, _, headers = self._insights_api.create_insight_with_http_info(
            project_owner, project_id, body=request, _return_http_data_only
            =False)
        if 'Location' in headers:
            return headers['Location']
    except _swagger.rest.ApiException as e:
        raise RestApiError(cause=e)