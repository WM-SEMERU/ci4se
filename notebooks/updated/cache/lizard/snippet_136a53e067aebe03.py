def get_object_header_view(self, request, url_kwargs, parent_only=False,
    render_type='object_header'):
    if parent_only and self.object_view != self.parent_attr:
        return None, None
    if self.object_view == self.parent_attr and self.parent:
        return self.parent.get_object_header_view(request, url_kwargs,
            render_type=render_type)
    elif self.object_view:
        view, name = self.get_initialized_view_and_name(self.object_view,
            can_submit=False, base_template='cms/partial.html', request=
            request, kwargs=url_kwargs, render_type=render_type)
        if view and view.can_view(request.user):
            return view, name
    return None, None