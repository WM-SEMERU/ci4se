def layer_icon(layer):
    if is_raster_layer(layer):
        return QgsLayerItem.iconRaster()
    elif is_point_layer(layer):
        return QgsLayerItem.iconPoint()
    elif is_line_layer(layer):
        return QgsLayerItem.iconLine()
    elif is_polygon_layer(layer):
        return QgsLayerItem.iconPolygon()
    else:
        return QgsLayerItem.iconDefault()