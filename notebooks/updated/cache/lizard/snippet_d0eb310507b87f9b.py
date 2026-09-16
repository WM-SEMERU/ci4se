def alterar(self, id_brand, name):
    if not is_valid_int_param(id_brand):
        raise InvalidParameterError(
            'The identifier of Brand is invalid or was not informed.')
    url = 'brand/' + str(id_brand) + '/'
    brand_map = dict()
    brand_map['name'] = name
    code, xml = self.submit({'brand': brand_map}, 'PUT', url)
    return self.response(code, xml)