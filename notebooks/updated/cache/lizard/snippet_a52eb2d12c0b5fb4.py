def _are_coordinates_valid(self):
    try:
        QgsPointXY(self.x_minimum.value(), self.y_maximum.value())
        QgsPointXY(self.x_maximum.value(), self.y_minimum.value())
    except ValueError:
        return False
    return True