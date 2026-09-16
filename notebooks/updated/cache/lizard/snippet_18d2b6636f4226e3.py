def validate_password_reset(cls, code, new_password):
    password_reset_model = PasswordResetModel.where_code(code)
    if password_reset_model is None:
        return None
    jwt = JWT()
    if jwt.verify_token(password_reset_model.token):
        user = cls.where_id(jwt.data['data']['user_id'])
        if user is not None:
            user.set_password(new_password)
            PasswordResetModel.delete_where_user_id(user.id)
            return user
    password_reset_model.delete()
    return None