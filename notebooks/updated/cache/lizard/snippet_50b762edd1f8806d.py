def get_listing_api(self, resource):
    get_all_params = self.get_listing_parameters(resource)
    get_all_api = {'path': '/%s/' % resource.get_api_name(), 'description':
        'Operations on %s' % resource.model.__name__, 'operations': [{
        'httpMethod': 'GET', 'nickname': 'list%ss' % resource.model.
        __name__, 'summary': 'Find %ss' % resource.model.__name__,
        'parameters': get_all_params}]}
    return get_all_api