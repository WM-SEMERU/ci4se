def get_jclass(classname):
    try:
        return javabridge.class_for_name(classname)
    except:
        return javabridge.static_call('Lweka/core/ClassHelper;', 'forName',
            '(Ljava/lang/Class;Ljava/lang/String;)Ljava/lang/Class;',
            javabridge.class_for_name('java.lang.Object'), classname)