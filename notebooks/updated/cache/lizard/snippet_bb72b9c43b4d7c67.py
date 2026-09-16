def loadLayer(filename, name=None, provider=None):
    name = name or os.path.splitext(os.path.basename(filename))[0]
    if provider != 'gdal':
        qgslayer = QgsVectorLayer(filename, name, provider or 'ogr')
    if provider == 'gdal' or not qgslayer.isValid():
        qgslayer = QgsRasterLayer(filename, name, provider or 'gdal')
        if not qgslayer.isValid():
            raise RuntimeError('Could not load layer: ' + unicode(filename))
    return qgslayer