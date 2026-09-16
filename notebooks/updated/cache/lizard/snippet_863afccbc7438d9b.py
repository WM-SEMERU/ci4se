def store_sm(smodel, filename, monitor):
    h5 = monitor.hdf5
    with monitor('store source model'):
        sources = h5['source_info']
        source_geom = h5['source_geom']
        gid = len(source_geom)
        for sg in smodel:
            if filename:
                with hdf5.File(filename, 'r+') as hdf5cache:
                    hdf5cache['grp-%02d' % sg.id] = sg
            srcs = []
            geoms = []
            for src in sg:
                srcgeom = src.geom()
                n = len(srcgeom)
                geom = numpy.zeros(n, point3d)
                geom['lon'], geom['lat'], geom['depth'] = srcgeom.T
                srcs.append((sg.id, src.source_id, src.code, gid, gid + n,
                    src.num_ruptures, 0, 0, 0))
                geoms.append(geom)
                gid += n
            if geoms:
                hdf5.extend(source_geom, numpy.concatenate(geoms))
            if sources:
                hdf5.extend(sources, numpy.array(srcs, source_info_dt))