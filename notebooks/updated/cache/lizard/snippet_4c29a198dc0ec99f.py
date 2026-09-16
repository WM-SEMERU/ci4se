def get_form_kwargs(self):
    data = super(UserContextFormViewMixin, self).get_form_kwargs()
    data.update({'user': self.get_agnocomplete_context()})
    return data