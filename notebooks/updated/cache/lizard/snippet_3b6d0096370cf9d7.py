def CreateMuskingumXFileFromDranageLine(in_drainage_line, x_id, out_x_file,
    file_geodatabase=None):
    ogr_drainage_line_shapefile_lyr, ogr_drainage_line_shapefile = (
        open_shapefile(in_drainage_line, file_geodatabase))
    with open_csv(out_x_file, 'w') as kfile:
        x_writer = csv_writer(kfile)
        for drainage_line_feature in ogr_drainage_line_shapefile_lyr:
            x_writer.writerow([drainage_line_feature.GetField(x_id)])
    del ogr_drainage_line_shapefile