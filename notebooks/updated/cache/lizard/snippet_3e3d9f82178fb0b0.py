def merge(file, feature_layers):
    tile = VectorTile(extents)
    for layer in feature_layers:
        tile.addFeatures(layer['features'], layer['name'])
    tile.complete()
    data = tile.out.SerializeToString()
    file.write(struct.pack('>I', len(data)))
    file.write(data)