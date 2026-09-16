def check_status_code(response, verbose):
    if response.status_code == 410 and response.url.startswith((
        'https://pypi.python.org', 'https://testpypi.python.org')):
        print(
            "It appears you're uploading to pypi.python.org (or testpypi.python.org). You've received a 410 error response. Uploading to those sites is deprecated. The new sites are pypi.org and test.pypi.org. Try using https://upload.pypi.org/legacy/ (or https://test.pypi.org/legacy/) to upload your packages instead. These are the default URLs for Twine now. More at https://packaging.python.org/guides/migrating-to-pypi-org/ "
            )
    try:
        response.raise_for_status()
    except HTTPError as err:
        if response.text:
            if verbose:
                print('Content received from server:\n{}'.format(response.text)
                    )
            else:
                print('NOTE: Try --verbose to see response content.')
        raise err