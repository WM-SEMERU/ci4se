def set_row_name(self, index, name):
    javabridge.call(self.jobject, 'setRowName', '(ILjava/lang/String;)V',
        index, name)