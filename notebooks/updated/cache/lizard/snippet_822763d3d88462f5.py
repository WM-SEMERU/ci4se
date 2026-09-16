def astra_volume_geometry(reco_space):
    if not isinstance(reco_space, DiscreteLp):
        raise TypeError('`reco_space` {!r} is not a DiscreteLp instance'.
            format(reco_space))
    if not reco_space.is_uniform:
        raise ValueError('`reco_space` {} is not uniformly discretized')
    vol_shp = reco_space.partition.shape
    vol_min = reco_space.partition.min_pt
    vol_max = reco_space.partition.max_pt
    if reco_space.ndim == 2:
        if not reco_space.partition.has_isotropic_cells and not astra_supports(
            'anisotropic_voxels_2d'):
            raise NotImplementedError(
                'non-isotropic pixels in 2d volumes not supported by ASTRA v{}'
                .format(ASTRA_VERSION))
        vol_geom = astra.create_vol_geom(vol_shp[0], vol_shp[1], vol_min[1],
            vol_max[1], -vol_max[0], -vol_min[0])
    elif reco_space.ndim == 3:
        if not reco_space.partition.has_isotropic_cells and not astra_supports(
            'anisotropic_voxels_3d'):
            raise NotImplementedError(
                'non-isotropic voxels in 3d volumes not supported by ASTRA v{}'
                .format(ASTRA_VERSION))
        vol_geom = astra.create_vol_geom(vol_shp[1], vol_shp[2], vol_shp[0],
            vol_min[2], vol_max[2], vol_min[1], vol_max[1], vol_min[0],
            vol_max[0])
    else:
        raise ValueError(
            '{}-dimensional volume geometries not supported by ASTRA'.
            format(reco_space.ndim))
    return vol_geom