def parse_optimize(self):
    match = re.search('EQUILIBRIUM GEOMETRY LOCATED', self.text)
    spmatch = 'SADDLE POINT LOCATED' in self.text
    located = True if match or spmatch else False
    points = grep_split(' BEGINNING GEOMETRY SEARCH POINT NSERCH=', self.text)
    if self.tddft == 'excite':
        points = [self.parse_energy(point) for point in points[1:]]
    else:
        regex = re.compile('NSERCH:\\s+\\d+\\s+E=\\s+([+-]?\\d+\\.\\d+)')
        points = [Energy(states=[State(0, None, float(m.group(1)), 0.0, 0.0
            )]) for m in regex.finditer(self.text)]
    if 'FAILURE TO LOCATE STATIONARY POINT, TOO MANY STEPS TAKEN' in self.text:
        self.errcode = GEOM_NOT_LOCATED
        self.errmsg = 'too many steps taken: %i' % len(points)
    if located:
        self.errcode = OK
    return Optimize(points=points)