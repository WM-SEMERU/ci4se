def use_project(self, project_id):
    return ProjectClient(base_uri=get_base_uri(project=project_id, host=
        self.host, port=self.port, secure=self.secure, api_base_path=self.
        api_base_path), auth_header=self.auth_header, requests_session=self
        .requests_session, request_defaults=self.request_defaults)