def add_json_mask(self, start, method_str, json_producer):

    def send_json(drh, rem_path):
        obj = json_producer(drh, rem_path)
        if not isinstance(obj, Response):
            obj = Response(obj)
        ctype = obj.get_ctype('application/json')
        code = obj.code
        obj = obj.response
        if obj is None:
            drh.send_error(404, 'File not found')
            return None
        f = BytesIO()
        json_str = json_dumps(obj)
        if isinstance(json_str, (str, unicode)):
            try:
                json_str = json_str.decode('utf8')
            except AttributeError:
                pass
            json_str = json_str.encode('utf8')
        f.write(json_str)
        f.flush()
        size = f.tell()
        f.seek(0)
        if drh.request_version >= 'HTTP/1.1':
            e_tag = '{0:x}'.format(zlib.crc32(f.read()) & 4294967295)
            f.seek(0)
            match = _getheader(drh.headers, 'if-none-match')
            if match is not None:
                if drh.check_cache(e_tag, match):
                    f.close()
                    return None
            drh.send_header('ETag', e_tag, end_header=True)
            drh.send_header('Cache-Control', 'max-age={0}'.format(self.
                max_age), end_header=True)
        drh.send_response(code)
        drh.send_header('Content-Type', ctype)
        drh.send_header('Content-Length', size)
        drh.end_headers()
        return f
    self._add_file_mask(start, method_str, send_json)