def is_dimensionless_standard_name(xml_tree, standard_name):
    if not isinstance(standard_name, basestring):
        return False
    found_standard_name = xml_tree.find(".//entry[@id='{}']".format(
        standard_name))
    if found_standard_name is not None:
        canonical_units = found_standard_name.find('canonical_units')
        dimless_units = '1(?:e-?(?:1|2|3|6|9|12|15|18|21|24))?$'
        return canonical_units is None or re.match(dimless_units,
            canonical_units.text)
    else:
        return False