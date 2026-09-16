def match_urls_to_resources(self, url_values):
    valid_values = {}
    for resource in self.Meta.related_resources:
        for k, v in url_values.items():
            resource_url = resource.get_resource_url(resource, resource.
                Meta.base_url)
            if isinstance(v, list):
                if all([(resource_url in i) for i in v]):
                    self.set_related_method(resource, v)
                    valid_values[k] = v
            elif resource_url in v:
                self.set_related_method(resource, v)
                valid_values[k] = v
    return valid_values