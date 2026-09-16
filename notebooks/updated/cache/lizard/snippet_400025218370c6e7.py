def draw_markers(self, data, coordinates, style, label, mplobj=None):
    vertices, pathcodes = style['markerpath']
    pathstyle = dict((key, style[key]) for key in ['alpha', 'edgecolor',
        'facecolor', 'zorder', 'edgewidth'])
    pathstyle['dasharray'] = '10,0'
    for vertex in data:
        self.draw_path(data=vertices, coordinates='points', pathcodes=
            pathcodes, style=pathstyle, offset=vertex, offset_coordinates=
            coordinates, mplobj=mplobj)