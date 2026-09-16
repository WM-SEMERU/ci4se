def delete(index_name, force, verbose):
    result = current_search_client.indices.delete(index=index_name, ignore=
        [400, 404] if force else None)
    if verbose:
        click.echo(json.dumps(result))