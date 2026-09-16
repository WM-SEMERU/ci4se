def _is_bval_type_a(grouped_dicoms):
    bval_tag = Tag(8193, 4099)
    bvec_x_tag = Tag(8197, 4272)
    bvec_y_tag = Tag(8197, 4273)
    bvec_z_tag = Tag(8197, 4274)
    for group in grouped_dicoms:
        if bvec_x_tag in group[0] and _is_float(common.get_fl_value(group[0
            ][bvec_x_tag])) and bvec_y_tag in group[0] and _is_float(common
            .get_fl_value(group[0][bvec_y_tag])) and bvec_z_tag in group[0
            ] and _is_float(common.get_fl_value(group[0][bvec_z_tag])
            ) and bval_tag in group[0] and _is_float(common.get_fl_value(
            group[0][bval_tag])) and common.get_fl_value(group[0][bval_tag]
            ) != 0:
            return True
    return False