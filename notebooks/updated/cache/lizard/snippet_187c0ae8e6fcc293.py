def _update_3d_datalim(ax, obj):
    min_bounding_box, max_bounding_box = geom.bounding_box(obj)
    xy_bounds = np.vstack((min_bounding_box[:COLS.Z], max_bounding_box[:
        COLS.Z]))
    ax.xy_dataLim.update_from_data_xy(xy_bounds, ignore=False)
    z_bounds = np.vstack(((min_bounding_box[COLS.Z], min_bounding_box[COLS.
        Z]), (max_bounding_box[COLS.Z], max_bounding_box[COLS.Z])))
    ax.zz_dataLim.update_from_data_xy(z_bounds, ignore=False)