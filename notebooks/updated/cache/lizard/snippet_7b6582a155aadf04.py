def get_version():
    version = 'Not installed.'
    try:
        version = pkg_resources.get_distribution(__package__).version
    except pkg_resources.DistributionNotFound:
        pass
    return version