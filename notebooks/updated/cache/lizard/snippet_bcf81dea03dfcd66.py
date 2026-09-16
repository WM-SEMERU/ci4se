def five_sided_box(size, rgba, group, thickness):
    geoms = []
    x, y, z = size
    r = thickness / 2
    geoms.append(new_geom(geom_type='box', size=[x, y, r], pos=[0, 0, -z +
        r], rgba=rgba, group=group))
    geoms.append(new_geom(geom_type='box', size=[x, r, z], pos=[0, -y + r, 
        0], rgba=rgba, group=group))
    geoms.append(new_geom(geom_type='box', size=[x, r, z], pos=[0, y - r, 0
        ], rgba=rgba, group=group))
    geoms.append(new_geom(geom_type='box', size=[r, y, z], pos=[x - r, 0, 0
        ], rgba=rgba, group=group))
    geoms.append(new_geom(geom_type='box', size=[r, y, z], pos=[-x + r, 0, 
        0], rgba=rgba, group=group))
    return geoms