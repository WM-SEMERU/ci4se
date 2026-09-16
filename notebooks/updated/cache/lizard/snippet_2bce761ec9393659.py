def read(self):
    r = c_int32()
    bufsize = self.npts * self.nchans
    inbuffer = np.zeros(bufsize)
    self.ReadAnalogF64(self.npts, 10.0, DAQmx_Val_GroupByChannel, inbuffer,
        bufsize, byref(r), None)
    self.WaitUntilTaskDone(10.0)
    return inbuffer.reshape(self.nchans, self.npts)