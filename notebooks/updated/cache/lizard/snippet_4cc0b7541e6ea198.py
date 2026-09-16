def get_context_data(self, **kwargs):
    context = super(BaseEntryChannel, self).get_context_data(**kwargs)
    context.update({'query': self.query})
    return context