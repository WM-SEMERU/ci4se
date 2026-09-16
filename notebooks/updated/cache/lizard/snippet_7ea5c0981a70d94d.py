def get_component(self, component_type):
    matching_components = list(filter(lambda component: isinstance(
        component, component_type), self._components))
    if matching_components:
        return matching_components[0]
    else:
        return None