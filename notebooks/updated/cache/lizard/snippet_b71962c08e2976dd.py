def keypairs(ctx, user_id, is_active):
    if ctx.invoked_subcommand is not None:
        return
    fields = [('User ID', 'user_id'), ('Access Key', 'access_key'), (
        'Secret Key', 'secret_key'), ('Active?', 'is_active'), ('Admin?',
        'is_admin'), ('Created At', 'created_at'), ('Last Used',
        'last_used'), ('Res.Policy', 'resource_policy'), ('Rate Limit',
        'rate_limit'), ('Concur.Limit', 'concurrency_limit'), (
        'Concur.Used', 'concurrency_used')]
    try:
        user_id = int(user_id)
    except (TypeError, ValueError):
        pass
    with Session() as session:
        try:
            items = session.KeyPair.list(user_id, is_active, fields=(item[1
                ] for item in fields))
        except Exception as e:
            print_error(e)
            sys.exit(1)
        if len(items) == 0:
            print(
                'There are no matching keypairs associated with the user ID {0}'
                .format(user_id))
            return
        print(tabulate((item.values() for item in items), headers=(item[0] for
            item in fields)))