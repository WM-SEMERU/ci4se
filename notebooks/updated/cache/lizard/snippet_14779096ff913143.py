def post_merge_request(profile, payload):
    repo = profile['repo']
    url = GITHUB_API_BASE_URL + 'repos/' + repo + '/merges'
    headers = get_headers(profile)
    response = requests.post(url, json=payload, headers=headers)
    return response