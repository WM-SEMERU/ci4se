def post(self, request, *args, **kwargs):
    versions = self._get_versions()
    url = self.get_done_url()
    msg = None
    try:
        vid = int(request.POST.get('version', ''))
        version = versions.get(vid=vid)
        if request.POST.get('revert'):
            object_url = self.get_object_url()
            msg = self.revert(version, object_url)
        elif request.POST.get('delete'):
            msg = self.delete(version)
            url = self.request.build_absolute_uri()
    except (ValueError, versions.model.DoesNotExist):
        pass
    return self.render(request, redirect_url=url, message=msg, obj=self.
        object, collect_render_data=False)