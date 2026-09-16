def check_ioc_countries(verbosity=1):
    from django_countries.data import COUNTRIES
    if verbosity:
        print('Checking if all IOC codes map correctly')
    for key in ISO_TO_IOC:
        assert COUNTRIES.get(key), 'No ISO code for %s' % key
    if verbosity:
        print('Finished checking IOC codes')