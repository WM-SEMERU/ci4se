def get_related_resource(_self, _Class, _ClassDataWrapper, *args, **kwargs):
    url = '%s/%s/%s' % (_self.resource_url(), _self.id, _Class.resource_url())
    response = json.loads(_self.marvel._call(url, _self.marvel._params(
        kwargs)).text)
    return _ClassDataWrapper(_self.marvel, response)