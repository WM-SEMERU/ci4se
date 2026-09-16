def validate_username(form, field):
    try:
        validate_username(field.data)
    except ValueError as e:
        raise ValidationError(e)
    try:
        user_profile = UserProfile.get_by_username(field.data)
        if (current_userprofile.is_anonymous or current_userprofile.user_id !=
            user_profile.user_id and field.data != current_userprofile.username
            ):
            raise ValidationError(_('Username already exists.'))
    except NoResultFound:
        return