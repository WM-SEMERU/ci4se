def upload(dist_dir):
    if 'PYPI_USER' in os.environ and 'PYPI_PASS' in os.environ:
        pypi_user = os.environ['PYPI_USER']
        pypi_pass = os.environ['PYPI_PASS']
    else:
        pypi_user = None
        pypi_pass = None
        print('No PYPI user information in environment')
    packages = glob.glob(dist_dir)
    twine_upload(packages, 'pypi', False, None, pypi_user, pypi_pass, None,
        None, '~/.pypirc', False, None, None, None)