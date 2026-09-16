def login_checking_email(pending_id, ticket, response, detail_url=
    'https://pswdless.appspot.com/rest/detail'):
    return LoginCheckingEmail(pending_id, ticket, response,
        USER_COOKIE_NAME, detail_url)