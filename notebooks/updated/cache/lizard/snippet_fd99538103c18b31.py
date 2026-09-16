def get_open_trackers_from_remote():
    url_base = (
        'https://raw.githubusercontent.com/idlesign/torrentool/master/torrentool/repo'
        )
    url = '%s/%s' % (url_base, OPEN_TRACKERS_FILENAME)
    try:
        import requests
        response = requests.get(url, timeout=REMOTE_TIMEOUT)
        response.raise_for_status()
        open_trackers = response.text.splitlines()
    except (ImportError, requests.RequestException) as e:
        raise RemoteDownloadError('Unable to download from %s: %s' % (url, e))
    return open_trackers