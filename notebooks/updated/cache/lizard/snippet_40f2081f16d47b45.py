def _create_list_of_array_controllers(self):
    headers, array_uri, array_settings = self._get_array_controller_resource()
    array_uri_links = []
    if 'links' in array_settings and 'Member' in array_settings['links']:
        array_uri_links = array_settings['links']['Member']
    else:
        msg = '"links/Member" section in ArrayControllers does not exist'
        raise exception.IloCommandNotSupportedError(msg)
    return array_uri_links