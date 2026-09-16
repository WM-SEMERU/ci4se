def createNorthPointer(self):
    self.headingNorthTri = patches.RegularPolygon((0.0, 0.8), 3, 0.05,
        color='k', zorder=4)
    self.axes.add_patch(self.headingNorthTri)
    self.headingNorthText = self.axes.text(0.0, 0.675, 'N', color='k', size
        =self.fontSize, horizontalalignment='center', verticalalignment=
        'center', zorder=4)