def load(fp, encode_nominal=False, return_type=DENSE):
    decoder = ArffDecoder()
    return decoder.decode(fp, encode_nominal=encode_nominal, return_type=
        return_type)