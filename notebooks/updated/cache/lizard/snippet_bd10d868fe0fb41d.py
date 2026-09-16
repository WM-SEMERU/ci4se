def generateMethods(self):
    for i in range(1, 5):
        self.make_grid_slot(i, i)
    for cl in self.mvision_classes:
        self.make_mvision_slot(cl)