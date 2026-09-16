def mimetype_params(self):

    def on_update(d):
        self.headers['Content-Type'] = dump_options_header(self.mimetype, d)
    d = parse_options_header(self.headers.get('content-type', ''))[1]
    return CallbackDict(d, on_update)