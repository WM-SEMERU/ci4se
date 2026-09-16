def delete(self, *args, **kwargs):
    self.model = self.get_model(kwargs.get('id'))
    result = yield self.model.fetch()
    if not result:
        self.not_found()
        return
    if not self.has_delete_permission():
        self.permission_denied()
        return
    self.model.delete()
    self.set_status(204)
    self.finish()