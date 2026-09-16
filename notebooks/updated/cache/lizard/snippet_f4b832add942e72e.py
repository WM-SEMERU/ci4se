def services_type(loader):

    def impl(string):
        t_services = loader.get_models('common.models#Services')
        if set(string) - set('bqtf'):
            raise ValueError
        return t_services(_str=''.join(set(string)))
    return impl