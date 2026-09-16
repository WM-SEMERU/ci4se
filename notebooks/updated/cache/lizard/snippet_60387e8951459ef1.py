def add_accounts_to_group(accounts_query, group):
    query = accounts_query.filter(date_deleted__isnull=True)
    for account in query:
        add_account_to_group(account, group)