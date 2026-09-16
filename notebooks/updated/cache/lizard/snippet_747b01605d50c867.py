def for_instances(cls, data, multi=None):
    if multi is None:
        return Capabilities(javabridge.static_call('weka/core/Capabilities',
            'forInstances',
            '(Lweka/core/Instances;)Lweka/core/Capabilities;', data.jobject))
    else:
        return Capabilities(javabridge.static_call('weka/core/Capabilities',
            'forInstances',
            '(Lweka/core/Instances;Z)Lweka/core/Capabilities;', data.
            jobject, multi))