def add_view(self, request, **kwargs):
    try:
        return super(ClonedRepoAdmin, self).add_view(request, **kwargs)
    except ValidationError:
        return redirect(request.path)