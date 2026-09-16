def Tensors(self, run, tag):
    accumulator = self.GetAccumulator(run)
    return accumulator.Tensors(tag)