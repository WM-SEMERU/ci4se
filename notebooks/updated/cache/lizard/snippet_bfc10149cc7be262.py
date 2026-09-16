def decrease_frequency(self, frequency=None):
    if frequency is None:
        javabridge.call(self.jobject, 'decreaseFrequency', '()V')
    else:
        javabridge.call(self.jobject, 'decreaseFrequency', '(I)V', frequency)