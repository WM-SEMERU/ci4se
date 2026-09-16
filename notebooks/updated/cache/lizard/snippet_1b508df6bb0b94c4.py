def post_request(profile, resource, payload):
    url = get_url(profile, resource)
    headers = get_headers(profile)
    response = requests.post(url, json=payload, headers=headers)
    return response.json()