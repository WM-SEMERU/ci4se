def create(index_name, body, force, verbose):
    result = current_search_client.indices.create(index=index_name, body=
        json.load(body), ignore=[400] if force else None)
    if verbose:
        click.echo(json.dumps(result))