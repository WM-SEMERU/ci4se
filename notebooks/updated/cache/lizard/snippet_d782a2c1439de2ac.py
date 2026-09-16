def get_initial(self):
    initial = super(SendEmailView, self).get_initial()
    form_data = self.request.session.get(EMAIL_VALIDATION_STR, {}).get(
        'form_data', {})
    if form_data:
        initial.update(form_data)
    return initial