def handle_error(self, error, url):
    if error.info is None or error.info.macaroon is None:
        raise BakeryException('unable to read info in discharge error response'
            )
    discharges = bakery.discharge_all(error.info.macaroon, self.
        acquire_discharge, self.key)
    macaroons = '[' + ','.join(map(utils.macaroon_to_json_string, discharges)
        ) + ']'
    all_macaroons = base64.urlsafe_b64encode(utils.to_bytes(macaroons))
    full_path = urljoin(url, error.info.macaroon_path)
    if error.info.cookie_name_suffix is not None:
        name = 'macaroon-' + error.info.cookie_name_suffix
    else:
        name = 'macaroon-auth'
    expires = checkers.macaroons_expiry_time(checkers.Namespace(), discharges)
    self.cookies.set_cookie(utils.cookie(name=name, value=all_macaroons.
        decode('ascii'), url=full_path, expires=expires))