def get_stdev(self, col, row):
    return javabridge.call(self.jobject, 'getStdDev', '(II)D', col, row)