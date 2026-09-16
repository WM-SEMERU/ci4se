def set_painter(self, painter, light_color):
    painter.setPen(QColor(light_color).darker(120))
    painter.setBrush(QBrush(QColor(light_color)))