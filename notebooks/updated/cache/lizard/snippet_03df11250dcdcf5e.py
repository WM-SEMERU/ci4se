def pretrained_run(self, d, x, ntrain=0.5, epochs=1):
    Ntrain = int(len(d) * ntrain)
    for epoch in range(epochs):
        self.run(d[:Ntrain], x[:Ntrain])
    y, e, w = self.run(d[Ntrain:], x[Ntrain:])
    return y, e, w