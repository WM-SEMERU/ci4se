def saver_for_file(filename):
    saver = javabridge.static_call('weka/core/converters/ConverterUtils',
        'getSaverForFile',
        '(Ljava/lang/String;)Lweka/core/converters/AbstractFileSaver;',
        filename)
    if saver is None:
        return None
    else:
        return Saver(jobject=saver)