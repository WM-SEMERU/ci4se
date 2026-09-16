def get_context(self):
    if not self.is_valid():
        raise ValueError('Cannot generate Context when form is invalid.')
    return dict(request=self.request, **self.cleaned_data)