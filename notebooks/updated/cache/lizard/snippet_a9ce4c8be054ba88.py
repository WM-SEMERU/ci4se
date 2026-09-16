def add(self, calc, module, package=None):
    super(Calculations, self).add(calc, module, package)
    if calc not in self.layer:
        self.layer[calc] = {'module': module, 'package': package}
    self.objects[calc] = self.sources[calc]()
    calc_src_obj = self.objects[calc]
    meta = [getattr(calc_src_obj, m) for m in self.reg.meta_names]
    self.reg.register(calc_src_obj.calcs, *meta)