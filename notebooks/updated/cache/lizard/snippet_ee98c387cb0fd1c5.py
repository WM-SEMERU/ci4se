def write_basic_mesh(Verts, E2V=None, mesh_type='tri', pdata=None, pvdata=
    None, cdata=None, cvdata=None, fname='output.vtk'):
    if E2V is None:
        mesh_type = 'vertex'
    map_type_to_key = {'vertex': 1, 'tri': 5, 'quad': 9, 'tet': 10, 'hex': 12}
    if mesh_type not in map_type_to_key:
        raise ValueError('unknown mesh_type=%s' % mesh_type)
    key = map_type_to_key[mesh_type]
    if mesh_type == 'vertex':
        uidx = np.arange(0, Verts.shape[0]).reshape((Verts.shape[0], 1))
        E2V = {key: uidx}
    else:
        E2V = {key: E2V}
    if cdata is not None:
        cdata = {key: cdata}
    if cvdata is not None:
        cvdata = {key: cvdata}
    write_vtu(Verts=Verts, Cells=E2V, pdata=pdata, pvdata=pvdata, cdata=
        cdata, cvdata=cvdata, fname=fname)