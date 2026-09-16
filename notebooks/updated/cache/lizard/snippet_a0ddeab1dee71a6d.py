def ng_delete(self, request, *args, **kwargs):
    if 'pk' not in request.GET:
        raise NgMissingParameterError('Object id is required to delete.')
    obj = self.get_object()
    response = self.build_json_response(obj)
    obj.delete()
    return response