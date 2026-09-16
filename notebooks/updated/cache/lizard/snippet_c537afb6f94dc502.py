def clear_components(self):
    ComponentRegistry._component_overlays = {}
    for key in self.list_components():
        self.remove_component(key)