def respond_server_error(self, status=None, status_line=None, message=None):
    ex_type, ex_value, ex_traceback = sys.exc_info()
    if ex_type:
        ex_file_name, ex_line, _, _ = traceback.extract_tb(ex_traceback)[-1]
        line_info = '{0}:{1}'.format(ex_file_name, ex_line)
        log_msg = 'encountered {0} in {1}'.format(repr(ex_value), line_info)
        self.server.logger.error(log_msg, exc_info=True)
    status = status or 500
    status_line = (status_line or http.client.responses.get(status,
        'Internal Server Error')).strip()
    self.send_response(status, status_line)
    message = message or status_line
    if isinstance(message, (str, bytes)):
        self.send_header('Content-Length', len(message))
        self.end_headers()
        if isinstance(message, str):
            self.wfile.write(message.encode(sys.getdefaultencoding()))
        else:
            self.wfile.write(message)
    elif hasattr(message, 'fileno'):
        fs = os.fstat(message.fileno())
        self.send_header('Content-Length', fs[6])
        self.end_headers()
        shutil.copyfileobj(message, self.wfile)
    else:
        self.end_headers()
    return