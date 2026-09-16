def clear(self):
    self.sampler.clear()
    self.samples_list = self._comm.gather(self.sampler.samples, root=0)
    if hasattr(self.sampler, 'weights'):
        self.weights_list = self._comm.gather(self.sampler.weights, root=0)
    else:
        self.weights_list = None