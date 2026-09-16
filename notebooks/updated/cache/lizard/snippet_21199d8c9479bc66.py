def add_accounts_to_project(accounts_query, project):
    query = accounts_query.filter(date_deleted__isnull=True)
    for account in query:
        add_account_to_project(account, project)