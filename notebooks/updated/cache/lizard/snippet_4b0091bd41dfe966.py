def create(config, group, type):
    if type not in ('user', 'service'):
        raise click.BadOptionUsage("--grouptype must be 'user' or 'service'")
    client = Client()
    client.prepare_connection()
    group_api = API(client)
    group_api.create(group, type)