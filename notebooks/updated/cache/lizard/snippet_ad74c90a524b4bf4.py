def _reproject(self, new_width, new_height, dest_affine, dtype=None,
    dst_crs=None, resampling=Resampling.cubic):
    if new_width == 0 or new_height == 0:
        return None
    dst_crs = dst_crs or self.crs
    dtype = dtype or self.image.data.dtype
    max_dtype_value = self._max_per_dtype(self.dtype)
    src_transform = self._patch_affine(self.affine)
    dst_transform = self._patch_affine(dest_affine)
    band_images = []
    for band_name in self.band_names:
        single_band_raster = self.bands_data([band_name])
        mask = np.ma.getmaskarray(single_band_raster)
        alpha = (~mask).astype(np.uint8) * max_dtype_value
        src_image = np.concatenate((single_band_raster.data, alpha))
        alpha_band_idx = 2
        dest_image = np.zeros([alpha_band_idx, new_height, new_width],
            dtype=self.dtype)
        rasterio.warp.reproject(src_image, dest_image, src_transform=
            src_transform, dst_transform=dst_transform, src_crs=self.crs,
            dst_crs=dst_crs, resampling=resampling, dest_alpha=
            alpha_band_idx, init_dest_nodata=False, src_alpha=alpha_band_idx)
        dest_image = np.ma.masked_array(dest_image[0:1, :, :], dest_image[1
            :2, :, :] == 0)
        band_images.append(dest_image)
    dest_image = np.ma.concatenate(band_images)
    new_raster = self.copy_with(image=np.ma.masked_array(dest_image.data,
        np.ma.getmaskarray(dest_image)), affine=dst_transform, crs=dst_crs)
    return new_raster