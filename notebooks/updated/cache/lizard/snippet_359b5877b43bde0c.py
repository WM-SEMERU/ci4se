def decode(dct, intype='json', raise_error=False):
    for decoder in get_plugins('decoders').values():
        if set(list(decoder.dict_signature)).issubset(dct.keys()) and hasattr(
            decoder, 'from_{}'.format(intype)) and getattr(decoder,
            'allow_other_keys', False):
            return getattr(decoder, 'from_{}'.format(intype))(dct)
            break
        elif sorted(list(decoder.dict_signature)) == sorted(dct.keys()
            ) and hasattr(decoder, 'from_{}'.format(intype)):
            return getattr(decoder, 'from_{}'.format(intype))(dct)
            break
    if raise_error:
        raise ValueError('no suitable plugin found for: {}'.format(dct))
    else:
        return dct