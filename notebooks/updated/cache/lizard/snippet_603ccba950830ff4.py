def get_filter(self, **filter_kwargs):
    q_objects = super(ListView, self).get_filter(**filter_kwargs)
    form = self.get_filter_form()
    if form:
        q_objects.extend(form.get_filter())
    return q_objects