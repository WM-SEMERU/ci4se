def generate(env):
    try:
        bld = env['BUILDERS']['Tar']
    except KeyError:
        bld = TarBuilder
        env['BUILDERS']['Tar'] = bld
    env['TAR'] = env.Detect(tars) or 'gtar'
    env['TARFLAGS'] = SCons.Util.CLVar('-c')
    env['TARCOM'] = '$TAR $TARFLAGS -f $TARGET $SOURCES'
    env['TARSUFFIX'] = '.tar'