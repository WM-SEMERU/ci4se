def get_app(self, reference_app=None):
    if reference_app is not None:
        return reference_app
    if current_app:
        return current_app._get_current_object()
    if self.app is not None:
        return self.app
    raise RuntimeError(
        'No application found. Either work inside a view function or push an application context. See http://flask-sqlalchemy.pocoo.org/contexts/.'
        )