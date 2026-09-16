def scale_meta_data_according_states(models_dict):
    left, right, top, bottom = get_boundaries_of_elements_in_dict(models_dict
        =models_dict)
    parent_size = models_dict['state'].parent.get_meta_data_editor()['size']
    _, rel_pos, size = cal_frame_according_boundaries(left, right, top,
        bottom, parent_size)
    models_dict['state'].set_meta_data_editor('rel_pos', rel_pos)
    models_dict['state'].set_meta_data_editor('size', size)
    offset = mult_two_vectors((-1.0, -1.0), rel_pos)
    offset_rel_pos_of_all_models_in_dict(models_dict, offset)
    return True