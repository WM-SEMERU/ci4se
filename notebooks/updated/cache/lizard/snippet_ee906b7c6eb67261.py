def custom_properties(self, props):
    fprops = javabridge.make_instance('java/io/File',
        '(Ljava/lang/String;)V', props)
    javabridge.call(self.jobject, 'setCustomPropsFile', '(Ljava/io/File;)V',
        fprops)