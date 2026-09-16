def transform_to_geographic(this_spec_meas_df, samp_df, samp, coord='0'):
    decs = this_spec_meas_df['dir_dec'].values.tolist()
    incs = this_spec_meas_df['dir_inc'].values.tolist()
    or_info, az_type = pmag.get_orient(samp_df, samp, data_model=3)
    if 'azimuth' in or_info.keys() and cb.not_null(or_info['azimuth'], False):
        azimuths = len(decs) * [or_info['azimuth']]
        dips = len(decs) * [or_info['dip']]
    else:
        return this_spec_meas_df
    dirs = [decs, incs, azimuths, dips]
    dirs_geo = np.array(list(map(list, list(zip(*dirs)))))
    decs, incs = pmag.dogeo_V(dirs_geo)
    if coord == '100' and 'bed_dip_direction' in or_info.keys() and or_info[
        'bed_dip_direction'] != '':
        bed_dip_dirs = len(decs) * [or_info['bed_dip_direction']]
        bed_dips = len(decs) * [or_info['bed_dip']]
        dirs = [decs, incs, bed_dip_dirs, bed_dips]
        dirs_tilt = np.array(list(map(list, list(zip(*dirs)))))
        decs, incs = pmag.dotilt_V(dirs_tilt)
    this_spec_meas_df['dir_dec'] = decs
    this_spec_meas_df['dir_inc'] = incs
    return this_spec_meas_df