def _goargs(self, ret, go_args):
    goids = set()
    go2color = {}
    re_gocolor = re.compile('(GO:\\d{7})((?:#[0-9a-fA-F]{6})?)')
    for go_arg in go_args:
        mtch = re_gocolor.match(go_arg)
        if mtch:
            goid, color = mtch.groups()
            goids.add(goid)
            if color:
                go2color[goid] = color
        else:
            print('WARNING: UNRECOGNIZED ARG({})'.format(go_arg))
    self._update_ret(ret, goids, go2color)