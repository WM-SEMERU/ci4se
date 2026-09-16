def _rewrite_geometry(geom, new_lines):
    new_geom = []
    x = 0
    y = 0
    for line in new_lines:
        moveto, endsat, lineto_cmds = line
        dx = moveto.x - x
        dy = moveto.y - y
        x = endsat.x
        y = endsat.y
        new_geom.append(9)
        new_geom.append(zigzag(dx))
        new_geom.append(zigzag(dy))
        new_geom.extend(lineto_cmds)
    del geom[:]
    geom.extend(new_geom)