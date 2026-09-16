def check_link(self, link):
    r = requests.get(CHECK_LINK_ENDPOINT + link)
    if r.status_code != 200:
        raise GfycatClientError('Unable to check the link', r.status_code)
    return r.json()