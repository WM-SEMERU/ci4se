def update_user_auth_stat(self, user, success=True):
    if not user.login_count:
        user.login_count = 0
    if not user.fail_login_count:
        user.fail_login_count = 0
    if success:
        user.login_count += 1
        user.fail_login_count = 0
    else:
        user.fail_login_count += 1
    user.last_login = datetime.datetime.now()
    self.update_user(user)