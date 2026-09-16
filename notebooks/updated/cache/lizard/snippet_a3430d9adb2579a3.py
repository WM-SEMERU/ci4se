def _request(self, method, path, server=None, **kwargs):
    while True:
        next_server = server or self._get_server()
        try:
            response = self.server_pool[next_server].request(method, path,
                username=self.username, password=self.password, schema=self
                .schema, **kwargs)
            redirect_location = response.get_redirect_location()
            if redirect_location and 300 <= response.status <= 308:
                redirect_server = _server_url(redirect_location)
                self._add_server(redirect_server)
                return self._request(method, path, server=redirect_server,
                    **kwargs)
            if not server and response.status in SRV_UNAVAILABLE_STATUSES:
                with self._lock:
                    self._drop_server(next_server, response.reason)
            else:
                return response
        except (urllib3.exceptions.MaxRetryError, urllib3.exceptions.
            ReadTimeoutError, urllib3.exceptions.SSLError, urllib3.
            exceptions.HTTPError, urllib3.exceptions.ProxyError) as ex:
            ex_message = _ex_to_message(ex)
            if server:
                raise ConnectionError('Server not available, exception: %s' %
                    ex_message)
            preserve_server = False
            if isinstance(ex, urllib3.exceptions.ProtocolError):
                preserve_server = any(t in [type(arg) for arg in ex.args] for
                    t in PRESERVE_ACTIVE_SERVER_EXCEPTIONS)
            if not preserve_server:
                with self._lock:
                    self._drop_server(next_server, ex_message)
        except Exception as e:
            raise ProgrammingError(_ex_to_message(e))