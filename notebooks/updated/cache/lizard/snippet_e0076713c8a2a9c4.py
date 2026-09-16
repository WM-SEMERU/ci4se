def get_user_brief():
    client = get_user_api()
    with catch_raise_api_exception():
        data, _, headers = client.user_self_with_http_info()
    ratelimits.maybe_rate_limit(client, headers)
    return data.authenticated, data.slug, data.email, data.name