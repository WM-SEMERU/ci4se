def create_insight(self, project_owner, project_id, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('callback'):
        return self.create_insight_with_http_info(project_owner, project_id,
            **kwargs)
    else:
        data = self.create_insight_with_http_info(project_owner, project_id,
            **kwargs)
        return data