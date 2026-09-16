def add(self, output, module, package=None):
    super(Outputs, self).add(output, module, package)
    if output not in self.layer:
        self.layer[output] = {'module': module, 'package': package}
    self.objects[output] = self.sources[output]()
    out_src_obj = self.objects[output]
    meta = [getattr(out_src_obj, m) for m in self.reg.meta_names]
    self.reg.register(out_src_obj.outputs, *meta)