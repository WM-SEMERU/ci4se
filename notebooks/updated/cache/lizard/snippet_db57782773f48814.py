def stdpUpdate(self, time, clearBuffer=False, onlyPlace=False):
    if clearBuffer:
        while len(self.activationBuffer) > 1:
            baseI, baseE, baseP, t = self.activationBuffer.popleft()
            for I, E, P, i in self.activationBuffer:
                t = (i - t) * self.dt
                self.sdtpKernels(t, I, E, baseI, baseE, baseP, onlyPlace=
                    onlyPlace)
    else:
        for I, E, P, i in reversed(self.activationBuffer):
            t = (i - time) * self.dt
            self.sdtpKernels(t, I, E, self.instantaneousI, self.
                instantaneous, self.activationsP, onlyPlace=onlyPlace)
        for I, E, P, i in self.activationBuffer:
            t = (time - i) * self.dt
            self.sdtpKernels(t, self.instantaneousI, self.instantaneous, I,
                E, P, onlyPlace=onlyPlace)
        self.activationBuffer.append((np.copy(self.instantaneousI), {k: np.
            copy(self.instantaneous[k]) for k in self.instantaneous}, np.
            copy(self.activationsP), time))