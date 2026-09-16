def modify_tag(self, name, description=None, servers=None, new_name=None):
    res = self._modify_tag(name, description, servers, new_name)
    return Tag(cloud_manager=self, **res['tag'])