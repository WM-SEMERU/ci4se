def createWPText(self):
    self.wpText = self.axes.text(self.leftPos + 1.5 * self.vertSize / 10.0,
        0.97 - 1.5 * self.vertSize + 0.5 * self.vertSize / 10.0,
        '0/0\n(0 m, 0 s)', color='w', size=self.fontSize, ha='left', va='top')
    self.wpText.set_path_effects([PathEffects.withStroke(linewidth=1,
        foreground='black')])