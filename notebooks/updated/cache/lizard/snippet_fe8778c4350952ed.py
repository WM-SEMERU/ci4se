def list_output_formats(type_list):
    out_format_list = []
    for type_item in type_list:
        item_format = default_output_format(type_item)
        out_format_list.append(item_format)
    return out_format_list