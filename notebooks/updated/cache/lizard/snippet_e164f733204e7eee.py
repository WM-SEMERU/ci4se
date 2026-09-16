def generate(env):
    c_file, cxx_file = SCons.Tool.createCFileBuilders(env)
    c_file.add_action('.l', LexAction)
    c_file.add_emitter('.l', lexEmitter)
    c_file.add_action('.lex', LexAction)
    c_file.add_emitter('.lex', lexEmitter)
    cxx_file.add_action('.lm', LexAction)
    cxx_file.add_emitter('.lm', lexEmitter)
    cxx_file.add_action('.ll', LexAction)
    cxx_file.add_emitter('.ll', lexEmitter)
    env['LEX'] = env.Detect('flex') or 'lex'
    env['LEXFLAGS'] = SCons.Util.CLVar('')
    env['LEXCOM'] = '$LEX $LEXFLAGS -t $SOURCES > $TARGET'