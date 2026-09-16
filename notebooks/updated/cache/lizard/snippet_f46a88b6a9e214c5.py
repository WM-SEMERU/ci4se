def get_src_builders(self, env):
    memo_key = id(env)
    try:
        memo_dict = self._memo['get_src_builders']
    except KeyError:
        memo_dict = {}
        self._memo['get_src_builders'] = memo_dict
    else:
        try:
            return memo_dict[memo_key]
        except KeyError:
            pass
    builders = []
    for bld in self.src_builder:
        if SCons.Util.is_String(bld):
            try:
                bld = env['BUILDERS'][bld]
            except KeyError:
                continue
        builders.append(bld)
    memo_dict[memo_key] = builders
    return builders