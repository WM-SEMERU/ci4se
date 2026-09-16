def export_obj(vertices, triangles, filename):
    with open(filename, 'w') as fh:
        for v in vertices:
            fh.write('v {} {} {}\n'.format(*v))
        for f in triangles:
            fh.write('f {} {} {}\n'.format(*(f + 1)))