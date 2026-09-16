def get_propety_by_name(pif, name):
    warn('This method has been deprecated in favor of get_property_by_name')
    return next((x for x in pif.properties if x.name == name), None)