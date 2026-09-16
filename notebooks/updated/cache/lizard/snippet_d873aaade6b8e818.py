def getDefaultStack(layer=None, axolotl=False, groups=True, media=True,
    privacy=True, profiles=True):
    allLayers = YowStackBuilder.getDefaultLayers(axolotl, groups=groups,
        media=media, privacy=privacy, profiles=profiles)
    if layer:
        allLayers = allLayers + (layer,)
    return YowStack(allLayers, reversed=False)