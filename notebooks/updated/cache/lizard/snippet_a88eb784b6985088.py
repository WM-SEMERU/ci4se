def layer(self, layer_name):
    uri = self.layer_uri(layer_name)
    layer = QgsVectorLayer(uri, layer_name, 'ogr')
    if not layer.isValid():
        layer = QgsRasterLayer(uri, layer_name)
        if not layer.isValid():
            return False
    monkey_patch_keywords(layer)
    return layer