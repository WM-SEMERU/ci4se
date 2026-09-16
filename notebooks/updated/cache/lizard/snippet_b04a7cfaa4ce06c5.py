def add_view(self, request, **kwargs):
    if self.model is Page:
        return HttpResponseRedirect(self.get_content_models()[0].add_url)
    return super(PageAdmin, self).add_view(request, **kwargs)