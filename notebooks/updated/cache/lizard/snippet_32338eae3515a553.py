def get_initialized_view_and_name(self, view_name, follow_parent=True, **
    extra_kwargs):
    view, name = self.get_view_and_name(view_name)
    if hasattr(view, 'as_view'):
        e = dict(extra_kwargs)
        e.update(**self._get_view_kwargs(view, view_name))
        e['name'] = view_name
        view = view(**e)
    elif isinstance(view, Bundle):
        view, name = view.get_initialized_view_and_name('main', **extra_kwargs)
    elif view == self.parent_attr and self.parent:
        if follow_parent:
            return self.parent.get_initialized_view_and_name(view_name, **
                extra_kwargs)
        else:
            view = None
            name = None
    return view, name