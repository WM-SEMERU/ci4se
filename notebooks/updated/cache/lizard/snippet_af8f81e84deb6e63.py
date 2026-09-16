def split_vector_ctype(ctype):
    if not is_vector_ctype(ctype):
        raise ValueError('The given ctype is not a vector type.')
    for vector_length in [2, 3, 4, 8, 16]:
        if ctype.endswith(str(vector_length)):
            vector_str_len = len(str(vector_length))
            return ctype[:-vector_str_len], int(ctype[-vector_str_len:])