def list_entitlements(owner, repo, page, page_size, show_tokens):
    client = get_entitlements_api()
    with catch_raise_api_exception():
        data, _, headers = client.entitlements_list_with_http_info(owner=
            owner, repo=repo, page=page, page_size=page_size, show_tokens=
            show_tokens)
    ratelimits.maybe_rate_limit(client, headers)
    page_info = PageInfo.from_headers(headers)
    entitlements = [ent.to_dict() for ent in data]
    return entitlements, page_info