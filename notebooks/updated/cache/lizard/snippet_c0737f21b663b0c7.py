def delta_e_cie1976(color1, color2):
    color1_vector = _get_lab_color1_vector(color1)
    color2_matrix = _get_lab_color2_matrix(color2)
    delta_e = color_diff_matrix.delta_e_cie1976(color1_vector, color2_matrix)[0
        ]
    return numpy.asscalar(delta_e)