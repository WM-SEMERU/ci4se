def embedManifestExeCheck(target, source, env):
    if env.get('WINDOWS_EMBED_MANIFEST', 0):
        manifestSrc = target[0].get_abspath() + '.manifest'
        if os.path.exists(manifestSrc):
            ret = embedManifestExeAction([target[0]], None, env)
            if ret:
                raise SCons.Errors.UserError(
                    'Unable to embed manifest into %s' % target[0])
            return ret
        else:
            print('(embed: no %s.manifest found; not embedding.)' % str(
                target[0]))
    return 0