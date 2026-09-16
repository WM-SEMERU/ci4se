def get_linked_version(doi):
    try:
        request = requests.head(to_url(doi))
        return request.headers.get('location')
    except RequestException:
        return None