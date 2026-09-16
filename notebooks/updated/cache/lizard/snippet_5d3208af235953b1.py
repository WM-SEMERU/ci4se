def generate_inverse_mapping(order):
    mapping = generate_mapping(order)
    inv_mapping = {}
    for key, value in mapping.items():
        inv_mapping[value] = key
    return inv_mapping