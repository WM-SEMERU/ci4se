def scaleFitWindow(self):
    e = 2.0
    w1 = self.centralWidget().width() - e
    h1 = self.centralWidget().height() - e
    a1 = w1 / h1
    w2 = self.canvas.pixmap.width() - 0.0
    h2 = self.canvas.pixmap.height() - 0.0
    a2 = w2 / h2
    return w1 / w2 if a2 >= a1 else h1 / h2