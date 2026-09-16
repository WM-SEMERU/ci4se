def get_non_compulsory_fields(layer_purpose, layer_subcategory=None):
    all_fields = get_fields(layer_purpose, layer_subcategory, replace_null=
        False)
    compulsory_field = get_compulsory_fields(layer_purpose, layer_subcategory)
    if compulsory_field in all_fields:
        all_fields.remove(compulsory_field)
    return all_fields