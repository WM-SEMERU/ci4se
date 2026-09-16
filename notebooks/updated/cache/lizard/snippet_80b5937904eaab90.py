def _get_swig_version(env, swig):
    swig = env.subst(swig)
    pipe = SCons.Action._subproc(env, SCons.Util.CLVar(swig) + ['-version'],
        stdin='devnull', stderr='devnull', stdout=subprocess.PIPE)
    if pipe.wait() != 0:
        return
    out = SCons.Util.to_str(pipe.stdout.read())
    match = re.search('SWIG Version\\s+(\\S+).*', out, re.MULTILINE)
    if match:
        if verbose:
            print('Version is:%s' % match.group(1))
        return match.group(1)
    elif verbose:
        print('Unable to detect version: [%s]' % out)