def loadLayerNoCrsDialog(filename, name=None, provider=None):
    settings = QSettings()
    prjSetting = settings.value('/Projections/defaultBehaviour')
    settings.setValue('/Projections/defaultBehaviour', '')
    prjSetting3 = settings.value('/Projections/defaultBehavior')
    settings.setValue('/Projections/defaultBehavior', '')
    layer = loadLayer(filename, name, provider)
    settings.setValue('/Projections/defaultBehaviour', prjSetting)
    settings.setValue('/Projections/defaultBehavior', prjSetting3)
    return layer