def get_form(self, form, name):
    kwargs = self.get_kwargs(form, name)
    form_class = self.get_form_class(form, name)
    composite_form = form_class(data=form.data if form.is_bound else None,
        files=form.files if form.is_bound else None, **kwargs)
    return composite_form