def save_to_rst(prefix, data):
    with open(find_full_name(prefix), 'w') as rst_file:
        rst_file.write(full_gpl_for_rst)
        rst_file.write(data)