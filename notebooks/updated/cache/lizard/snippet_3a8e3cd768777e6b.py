def download_decode(URL, encoding='utf-8', verbose=True):
    if verbose:
        print('Downloading data from ' + URL)
    req = Request(URL)
    try:
        with urlopen(req) as u:
            decoded_file = u.read().decode(encoding)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('Server could not be reached.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print("The server couldn't fulfill the request.")
            print('Error code: ', e.code)
        return None
    return decoded_file