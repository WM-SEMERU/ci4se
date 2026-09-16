def get_user(self, user):
    self.project_service.set_auth(self._token_project)
    return self.project_service.get_user(user)