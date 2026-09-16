def disabledBrush(self):
    grad = QLinearGradient()
    rect = self.rect()
    grad.setStart(QPointF(0, rect.y()))
    grad.setFinalStop(QPointF(0, rect.bottom()))
    grad.setColorAt(0, self.disabledColor())
    grad.setColorAt(1, self.disabledAlternateColor())
    return QBrush(grad)