def skimage_radon_back_projector(sinogram, geometry, range, out=None):
    from skimage.transform import iradon
    theta = skimage_theta(geometry)
    skimage_range = skimage_sinogram_space(geometry, range, sinogram.space)
    skimage_sinogram = skimage_range.element()
    skimage_sinogram.sampling(clamped_interpolation(range, sinogram))
    if out is None:
        out = range.element()
    else:
        assert out in range
    backproj = iradon(skimage_sinogram.asarray().T, theta, output_size=
        range.shape[0], filter=None, circle=False)
    out[:] = np.rot90(backproj, -1)
    scaling_factor = 4.0 * float(geometry.motion_params.length) / (2 * np.pi)
    proj_extent = float(sinogram.space.partition.extent.prod())
    proj_size = float(sinogram.space.partition.size)
    proj_weighting = proj_extent / proj_size
    scaling_factor *= sinogram.space.weighting.const / proj_weighting
    scaling_factor /= range.weighting.const / range.cell_volume
    out *= scaling_factor
    return out