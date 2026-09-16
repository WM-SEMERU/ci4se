def create_header_from_telpars(telpars):
    pars = [val.strip() for val in ';'.join(telpars).split(';') if val.
        strip() != '']
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', fits.verify.VerifyWarning)
        hdr = fits.Header(map(parse_hstring, pars))
    return hdr