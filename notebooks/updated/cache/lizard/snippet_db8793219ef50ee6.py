def render_to_response(self, context, **response_kwargs):
    filename = os.path.basename(self.object.file.name)
    content_type, _ = mimetypes.guess_type(self.object.file.name)
    if not content_type:
        content_type = 'text/plain'
    response = HttpResponse(self.object.file, content_type=content_type)
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename
        )
    return response