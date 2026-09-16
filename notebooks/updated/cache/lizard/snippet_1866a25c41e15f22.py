def CreateWeightTableLDAS(in_ldas_nc, in_nc_lon_var, in_nc_lat_var,
    in_catchment_shapefile, river_id, in_connectivity_file,
    out_weight_table, area_id=None, file_geodatabase=None):
    data_ldas_nc = Dataset(in_ldas_nc)
    variables_list = data_ldas_nc.variables.keys()
    if in_nc_lon_var not in variables_list:
        raise Exception('Invalid longitude variable. Choose from: {0}'.
            format(variables_list))
    if in_nc_lat_var not in variables_list:
        raise Exception('Invalid latitude variable. Choose from: {0}'.
            format(variables_list))
    ldas_lon = data_ldas_nc.variables[in_nc_lon_var][:]
    ldas_lat = data_ldas_nc.variables[in_nc_lat_var][:]
    data_ldas_nc.close()
    rtree_create_weight_table(ldas_lat, ldas_lon, in_catchment_shapefile,
        river_id, in_connectivity_file, out_weight_table, file_geodatabase,
        area_id)