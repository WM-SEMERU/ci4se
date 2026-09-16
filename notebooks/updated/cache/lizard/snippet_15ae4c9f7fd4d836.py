def verify_email(self, action_token, signed_data):
    try:
        action = 'verify-email'
        user = get_user_by_action_token(action, action_token)
        if not user or not user.signed_data_match(signed_data, action):
            raise mocha_exc.AppError('Verification Invalid!')
        else:
            user.set_email_verified(True)
            flash_success('Account verified. You can now login')
            username = user.username
            if user.login_method == 'email':
                username = user.email
            return redirect(self.login, username=username)
    except Exception as e:
        logging.exception(e)
        flash_error('Verification Failed!')
    return redirect(self.login)