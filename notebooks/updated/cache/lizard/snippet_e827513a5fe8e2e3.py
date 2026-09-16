def validate_csrf_token(self, field):
    if current_app.testing:
        return
    super(InvenioBaseForm, self).validate_csrf_token(field)