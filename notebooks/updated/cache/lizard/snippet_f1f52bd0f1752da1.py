def get_resources_to_check(client_site_url, apikey):
    url = client_site_url + 'deadoralive/get_resources_to_check'
    response = requests.get(url, headers=dict(Authorization=apikey))
    if not response.ok:
        raise CouldNotGetResourceIDsError(
            "Couldn't get resource IDs to check: {code} {reason}".format(
            code=response.status_code, reason=response.reason))
    return response.json()