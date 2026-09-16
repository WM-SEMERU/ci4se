def origin_req_host(self):
    if self.history:
        return self.history[0].request.origin_req_host
    else:
        return scheme_host_port(self.url)[1]