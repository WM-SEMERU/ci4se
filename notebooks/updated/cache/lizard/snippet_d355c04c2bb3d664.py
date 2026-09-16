def _get_api_urls(self, api_urls=None):
    view_name = self.__class__.__name__
    api_urls = api_urls or {}
    api_urls['read'] = url_for(view_name + '.api_read')
    api_urls['delete'] = url_for(view_name + '.api_delete', pk='')
    api_urls['create'] = url_for(view_name + '.api_create')
    api_urls['update'] = url_for(view_name + '.api_update', pk='')
    return api_urls