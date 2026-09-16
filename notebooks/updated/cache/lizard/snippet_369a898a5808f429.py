def parse_params(self, ngpu=1, **kwargs):
    return_status = super(MadryEtAlMultiGPU, self).parse_params(**kwargs)
    self.ngpu = ngpu
    return return_status