def edit_view(self, request, object_id):
    kwargs = {'model_admin': self, 'object_id': object_id}
    view_class = self.edit_view_class
    return view_class.as_view(**kwargs)(request)