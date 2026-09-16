def layer_uri(self, layer_name):
    layers = self.layers()
    for layer, extension in product(layers, EXTENSIONS):
        one_file = QFileInfo(self.uri.filePath(layer + '.' + extension))
        if one_file.exists():
            if one_file.baseName() == layer_name:
                return one_file.absoluteFilePath()
    else:
        return None