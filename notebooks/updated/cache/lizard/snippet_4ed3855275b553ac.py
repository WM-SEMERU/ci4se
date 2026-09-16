def add_components(self, components):
    if components:
        for component in components:
            self._components[component['name']] = component['factory'
                ], component.get('properties', {})