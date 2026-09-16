def __apply_func(self, other, func_name):
    if isinstance(other, Signal):
        if len(self) and len(other):
            start = max(self.timestamps[0], other.timestamps[0])
            stop = min(self.timestamps[-1], other.timestamps[-1])
            s1 = self.cut(start, stop)
            s2 = other.cut(start, stop)
        else:
            s1 = self
            s2 = other
        time = np.union1d(s1.timestamps, s2.timestamps)
        s = self.interp(time).samples
        o = other.interp(time).samples
        func = getattr(s, func_name)
        s = func(o)
    elif other is None:
        s = self.samples
        time = self.timestamps
    else:
        func = getattr(self.samples, func_name)
        s = func(other)
        time = self.timestamps
    return Signal(samples=s, timestamps=time, unit=self.unit, name=self.
        name, conversion=self.conversion, raw=self.raw, master_metadata=
        self.master_metadata, display_name=self.display_name, attachment=
        self.attachment, stream_sync=self.stream_sync, invalidation_bits=
        self.invalidation_bits, source=self.source, encoding=self.encoding)