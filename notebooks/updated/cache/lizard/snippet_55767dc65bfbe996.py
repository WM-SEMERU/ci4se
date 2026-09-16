def remove_post_data_parameters(request, post_data_parameters_to_remove):
    replacements = [(k, None) for k in post_data_parameters_to_remove]
    return replace_post_data_parameters(request, replacements)