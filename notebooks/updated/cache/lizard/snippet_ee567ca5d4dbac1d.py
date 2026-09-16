def delete(self, request):
    if not self.can_delete:
        raise muffin.HTTPMethodNotAllowed()
    if not self.resource:
        raise muffin.HTTPNotFound(reason='Resource not found')
    self.resource.delete_instance()