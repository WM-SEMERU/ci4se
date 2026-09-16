def generate(env):
    as_module.generate(env)
    env['AS'] = '386asm'
    env['ASFLAGS'] = SCons.Util.CLVar('')
    env['ASPPFLAGS'] = '$ASFLAGS'
    env['ASCOM'] = '$AS $ASFLAGS $SOURCES -o $TARGET'
    env['ASPPCOM'] = (
        '$CC $ASPPFLAGS $CPPFLAGS $_CPPDEFFLAGS $_CPPINCFLAGS $SOURCES -o $TARGET'
        )
    addPharLapPaths(env)