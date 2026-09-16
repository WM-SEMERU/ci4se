def from_bytes(cls, image_bytes, affine, crs, band_names=None):
    b = io.BytesIO(image_bytes)
    image = imageio.imread(b)
    roll = np.rollaxis(image, 2)
    if band_names is None:
        band_names = [0, 1, 2]
    elif isinstance(band_names, str):
        band_names = [band_names]
    return GeoRaster2(image=roll[:3, :, :], affine=affine, crs=crs,
        band_names=band_names)