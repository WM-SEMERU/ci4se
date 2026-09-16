def create_subnode(self, data):
    return self.__class__(data, axis=self.sel_axis(self.axis), sel_axis=
        self.sel_axis, dimensions=self.dimensions)