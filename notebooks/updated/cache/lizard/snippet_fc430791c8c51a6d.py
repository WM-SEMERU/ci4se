def load_file(self, dfile, incremental=False):
    self.enforce_type(self.jobject, 'weka.core.converters.FileSourcedConverter'
        )
    self.incremental = incremental
    if not javabridge.is_instance_of(dfile, 'Ljava/io/File;'):
        dfile = javabridge.make_instance('Ljava/io/File;',
            '(Ljava/lang/String;)V', javabridge.get_env().new_string_utf(
            str(dfile)))
    javabridge.call(self.jobject, 'reset', '()V')
    sfile = javabridge.to_string(dfile)
    if not os.path.exists(sfile):
        raise Exception('Dataset file does not exist: ' + str(sfile))
    javabridge.call(self.jobject, 'setFile', '(Ljava/io/File;)V', dfile)
    if incremental:
        self.structure = Instances(javabridge.call(self.jobject,
            'getStructure', '()Lweka/core/Instances;'))
        return self.structure
    else:
        return Instances(javabridge.call(self.jobject, 'getDataSet',
            '()Lweka/core/Instances;'))