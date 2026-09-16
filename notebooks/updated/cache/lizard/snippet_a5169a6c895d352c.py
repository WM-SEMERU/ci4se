def get_owner_repos_url(owner, token):
    url_org = GITHUB_API_URL + '/orgs/' + owner + '/repos'
    url_user = GITHUB_API_URL + '/users/' + owner + '/repos'
    url_owner = url_org
    try:
        r = requests.get(url_org, params=get_payload(), headers=get_headers
            (token))
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if r.status_code == 403:
            rate_limit_reset_ts = datetime.fromtimestamp(int(r.headers[
                'X-RateLimit-Reset']))
            seconds_to_reset = (rate_limit_reset_ts - datetime.utcnow()
                ).seconds + 1
            logging.info(
                'GitHub rate limit exhausted. Waiting %i secs for rate limit reset.'
                 % seconds_to_reset)
            sleep(seconds_to_reset)
        else:
            url_owner = url_user
    return url_owner