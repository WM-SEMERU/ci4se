def fill_layer_combo(self):
    project = QgsProject.instance()
    layers = list(project.mapLayers().values())
    extensions = tuple(extension_siblings.keys())
    for layer in layers:
        if layer.source().lower().endswith(extensions):
            icon = layer_icon(layer)
            self.layers.addItem(icon, layer.name(), layer.id())