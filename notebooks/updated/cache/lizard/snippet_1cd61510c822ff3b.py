def wkt_to_rectangle(extent):
    geometry = QgsGeometry.fromWkt(extent)
    if not geometry.isGeosValid():
        return None
    polygon = geometry.asPolygon()[0]
    if len(polygon) != 5:
        return None
    if polygon[0] != polygon[4]:
        return None
    rectangle = QgsRectangle(QgsPointXY(polygon[0].x(), polygon[0].y()),
        QgsPointXY(polygon[2].x(), polygon[2].y()))
    return rectangle