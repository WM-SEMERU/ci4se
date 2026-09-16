def default_token_user_loader(self, token):
    try:
        data = self.decode_token(token)
    except jwt.exceptions.DecodeError as e:
        raise x.JwtDecodeError(str(e))
    except jwt.ExpiredSignatureError as e:
        raise x.JwtExpired(str(e))
    user = self.get(data['user_id'])
    if not user:
        msg = 'No user with such id [{}]'
        raise x.JwtNoUser(msg.format(data['user_id']))
    if user.is_locked():
        msg = 'This account is locked'
        raise x.AccountLocked(msg, locked_until=user.locked_until)
    if self.require_confirmation and not user.email_confirmed:
        msg = 'Please confirm your email address [{}]'
        raise x.EmailNotConfirmed(msg.format(user.email_secure), email=user
            .email)
    if not token == user._token:
        raise x.JwtTokenMismatch('The token does not match our records')
    return user