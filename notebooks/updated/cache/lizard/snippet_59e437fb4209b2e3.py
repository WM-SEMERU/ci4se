def make_template_name(self, model_type, sourcekey):
    format_dict = self.__dict__.copy()
    format_dict['sourcekey'] = sourcekey
    if model_type == 'IsoSource':
        return self._name_factory.spectral_template(**format_dict)
    elif model_type in ['MapCubeSource', 'SpatialMap']:
        return self._name_factory.diffuse_template(**format_dict)
    else:
        raise ValueError('Unexpected model_type %s' % model_type)