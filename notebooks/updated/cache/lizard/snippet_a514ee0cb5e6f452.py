def find_users_by_email_starting_with(email_prefix=None, cursor=None,
    page_size=30):
    email_prefix = email_prefix or ''
    return ModelSearchCommand(MainUser.query_email_starts_with(email_prefix
        ), page_size, cursor, cache_begin=None)