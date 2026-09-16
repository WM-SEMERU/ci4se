def get_resource_component_and_children(self, resource_id, resource_type=
    'collection', level=1, sort_data={}, recurse_max_level=False, sort_by=
    None, **kwargs):
    resource_type = self.resource_type(resource_id)
    if resource_type == 'resource':
        return self._get_resources(resource_id, recurse_max_level=
            recurse_max_level, sort_by=sort_by)
    else:
        return self._get_components(resource_id, recurse_max_level=
            recurse_max_level, sort_by=sort_by)