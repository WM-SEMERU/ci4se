def _rdtxt_gos(self, ret, go_file):
    if not os.path.exists(go_file):
        raise RuntimeError('CAN NOT READ: {FILE}\n'.format(FILE=go_file))
    goids = set()
    go2color = {}
    with open(go_file) as ifstrm:
        for line in ifstrm:
            goids_found = self.re_goids.findall(line)
            if goids_found:
                goids.update(goids_found)
                colors = self.re_color.findall(line)
                if colors:
                    if len(goids_found) == len(colors):
                        for goid, color in zip(goids_found, colors):
                            go2color[goid] = color
                    else:
                        print('IGNORING: {L}'.format(L=line))
    self._update_ret(ret, goids, go2color)