def replace_insight(self, project_key, insight_id, **kwargs):
    request = self.__build_insight_obj(lambda : _swagger.InsightPutRequest(
        title=kwargs.get('title'), body=_swagger.InsightBody(image_url=
        kwargs.get('image_url'), embed_url=kwargs.get('embed_url'),
        markdown_body=kwargs.get('markdown_body'))), kwargs)
    project_owner, project_id = parse_dataset_key(project_key)
    try:
        self._insights_api.replace_insight(project_owner, project_id,
            insight_id, body=request)
    except _swagger.rest.ApiException as e:
        raise RestApiError(cause=e)