def _apply_dvs_product_info(product_info_spec, product_info_dict):
    if product_info_dict.get('name'):
        product_info_spec.name = product_info_dict['name']
    if product_info_dict.get('vendor'):
        product_info_spec.vendor = product_info_dict['vendor']
    if product_info_dict.get('version'):
        product_info_spec.version = product_info_dict['version']