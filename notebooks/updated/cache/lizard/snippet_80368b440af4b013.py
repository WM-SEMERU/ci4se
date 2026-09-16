def increase_frequency(self, frequency=None):
    if frequency is None:
        javabridge.call(self.jobject, 'increaseFrequency', '()V')
    else:
        javabridge.call(self.jobject, 'increaseFrequency', '(I)V', frequency)