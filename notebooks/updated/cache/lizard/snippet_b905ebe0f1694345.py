def normal_surface_single_list(obj, param_list, normalize):
    ret_vector = []
    for param in param_list:
        temp = normal_surface_single(obj, param, normalize)
        ret_vector.append(temp)
    return tuple(ret_vector)