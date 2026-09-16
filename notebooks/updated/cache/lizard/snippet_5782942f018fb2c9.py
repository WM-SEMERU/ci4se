def parse_api_groups(self, request_resources=False, update=False):
    if not self._cache.get('resources') or update:
        self._cache['resources'] = self._cache.get('resources', {})
        groups_response = load_json(self.client.request('GET', '/{}'.format
            (DISCOVERY_PREFIX)))['groups']
        groups = self.default_groups(request_resources=request_resources)
        for group in groups_response:
            new_group = {}
            for version_raw in group['versions']:
                version = version_raw['version']
                resource_group = self._cache.get('resources', {}).get(
                    DISCOVERY_PREFIX, {}).get(group['name'], {}).get(version)
                preferred = version_raw == group['preferredVersion']
                resources = resource_group.resources if resource_group else {}
                if request_resources:
                    resources = self.get_resources_for_api_version(
                        DISCOVERY_PREFIX, group['name'], version, preferred)
                new_group[version] = ResourceGroup(preferred, resources=
                    resources)
            groups[DISCOVERY_PREFIX][group['name']] = new_group
        self._cache['resources'].update(groups)
        self._write_cache()
    return self._cache['resources']