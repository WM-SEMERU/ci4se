def calc_extensions(self, extensions=None, Y_agg=None):
    ext_list = list(self.get_extensions(data=False))
    extensions = extensions or ext_list
    if type(extensions) == str:
        extensions = [extensions]
    for ext_name in extensions:
        self.meta._add_modify('Calculating accounts for extension {}'.
            format(ext_name))
        ext = getattr(self, ext_name)
        ext.calc_system(x=self.x, Y=self.Y, L=self.L, Y_agg=Y_agg,
            population=self.population)
    return self