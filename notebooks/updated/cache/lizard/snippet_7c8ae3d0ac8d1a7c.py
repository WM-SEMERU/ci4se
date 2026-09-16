def move_package(owner, repo, identifier, destination):
    client = get_packages_api()
    with catch_raise_api_exception():
        data, _, headers = client.packages_move_with_http_info(owner=owner,
            repo=repo, identifier=identifier, data={'destination': destination}
            )
    ratelimits.maybe_rate_limit(client, headers)
    return data.slug_perm, data.slug