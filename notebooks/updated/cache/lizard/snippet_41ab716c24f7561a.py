def openpnm_to_im(network, pore_shape='sphere', throat_shape='cylinder',
    max_dim=None, verbose=1, rtol=0.1):
    r
    return generate_voxel_image(network, pore_shape=pore_shape,
        throat_shape=throat_shape, max_dim=max_dim, verbose=verbose, rtol=rtol)