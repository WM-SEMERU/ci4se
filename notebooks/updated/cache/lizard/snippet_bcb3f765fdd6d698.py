def send_login_email(app_id, token, hook, email=None, user_id=None, lang=
    'en_US', url_login='https://pswdless.appspot.com/rest/login'):
    return SendLoginEmail(app_id, token, hook, email, user_id, lang, url_login)