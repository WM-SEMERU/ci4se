def _parse_bands(self, band_input):
    all_bands = (AwsConstants.S2_L1C_BANDS if self.data_source is
        DataSource.SENTINEL2_L1C else AwsConstants.S2_L2A_BANDS)
    if band_input is None:
        return all_bands
    if isinstance(band_input, str):
        band_list = band_input.split(',')
    elif isinstance(band_input, list):
        band_list = band_input.copy()
    else:
        raise ValueError('bands parameter must be a list or a string')
    band_list = [band.strip().split('.')[0] for band in band_list]
    band_list = [band for band in band_list if band != '']
    if not set(band_list) <= set(all_bands):
        raise ValueError('bands {} must be a subset of {}'.format(band_list,
            all_bands))
    return band_list