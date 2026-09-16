def _check_user(self, user):
    MissingUserError.require_condition(user is not None,
        'Could not find the requested user')
    user_validate_method = getattr(user, self.user_class_validation_method,
        None)
    if user_validate_method is None:
        return
    InvalidUserError.require_condition(user_validate_method(),
        'The user is not valid or has had access revoked')