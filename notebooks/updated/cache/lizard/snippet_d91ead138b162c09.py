def _callback_factory(callback_imp):
    if callback_imp is None:
        try:
            pkg_resources.get_distribution('flask-login')
            from flask_login import current_user
            return lambda : current_user.is_authenticated
        except pkg_resources.DistributionNotFound:
            return lambda : False
    elif isinstance(callback_imp, string_types):
        return import_string(callback_imp)
    else:
        return callback_imp