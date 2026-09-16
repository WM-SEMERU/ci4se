def users(accountable, query):
    users = accountable.users(query)
    headers = ['display_name', 'key']
    if users:
        rows = [[v for k, v in sorted(u.items()) if k in headers] for u in
            users]
        rows.insert(0, headers)
        print_table(SingleTable(rows))
    else:
        click.secho('No users found for query {}'.format(query), fg='red')