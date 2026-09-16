def generate(env):
    SCons.Tool.createSharedLibBuilder(env)
    SCons.Tool.createProgBuilder(env)
    env['LINK'] = '$CC'
    env['LINKFLAGS'] = SCons.Util.CLVar('')
    env['LINKCOM'] = '$LINK -q $LINKFLAGS -e$TARGET $SOURCES $LIBS'
    env['LIBDIRPREFIX'] = ''
    env['LIBDIRSUFFIX'] = ''
    env['LIBLINKPREFIX'] = ''
    env['LIBLINKSUFFIX'] = '$LIBSUFFIX'