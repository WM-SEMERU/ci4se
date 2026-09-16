def scan_codes(code_types, image):
    if isinstance(code_types, str):
        code_types = [code_types]
        warnings.warn(
            'Using a str for code_types is deprecated, please use a list of str instead'
            , DeprecationWarning)
    symbologies = [Symbologies.get(code_type.upper()) for code_type in set(
        code_types)]
    if None in symbologies:
        bad_code_types = [code_type for code_type in code_types if 
            code_type.upper() not in Symbologies]
        raise UnknownSymbologieError('Unknown Symbologies: %s' % bad_code_types
            )
    if not Image.isImageType(image):
        raise RuntimeError('Bad or unknown image format')
    converted_image = image.convert('L')
    raw = converted_image.tobytes()
    width, height = converted_image.size
    return zbar_code_scanner(symbologies, raw, width, height)