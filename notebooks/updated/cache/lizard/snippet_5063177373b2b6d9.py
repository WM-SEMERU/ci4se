def __replace_coord_variables(text, x_and_y, req_len, idx):
    return ResourceConfig.__replace_base_variables(text, req_len, idx).replace(
        '{xy}', str(x_and_y)).replace('{pi}', str(math.pi))