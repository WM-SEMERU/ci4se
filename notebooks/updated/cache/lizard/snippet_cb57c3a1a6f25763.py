def run(self, *args):
    params = self.parser.parse_args(args)
    ct = params.code_or_term
    if ct and len(ct) < 2:
        self.error('Code country or term must have 2 or more characters length'
            )
        return CODE_INVALID_FORMAT_ERROR
    code = ct if ct and len(ct) == 2 else None
    term = ct if ct and len(ct) > 2 else None
    try:
        countries = api.countries(self.db, code=code, term=term)
        self.display('countries.tmpl', countries=countries)
    except (NotFoundError, InvalidValueError) as e:
        self.error(str(e))
        return e.code
    return CMD_SUCCESS