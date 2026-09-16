def license(self, key, value):

    def _get_license(value):
        a_values = force_list(value.get('a'))
        oa_licenses = [el for el in a_values if el == 'OA' or el ==
            'Open Access']
        other_licenses = [el for el in a_values if el != 'OA' and el !=
            'Open Access']
        if not other_licenses:
            return force_single_element(oa_licenses)
        return force_single_element(other_licenses)

    def _get_material(value):
        material = value.get('3', '').lower()
        if material == 'article':
            return 'publication'
        return material
    return {'imposing': value.get('b'), 'license': _get_license(value),
        'material': _get_material(value), 'url': value.get('u')}