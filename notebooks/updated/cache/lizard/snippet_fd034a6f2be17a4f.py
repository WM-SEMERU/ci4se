def get_quote(self, code, as_json=False):
    code = code.upper()
    if self.is_valid_code(code):
        url = self.build_url_for_quote(code)
        req = Request(url, None, self.headers)
        res = self.opener.open(req)
        res = byte_adaptor(res)
        res = res.read()
        match = re.search(
            '<div\\s+id="responseDiv"\\s+style="display:none">(.*?)</div>',
            res, re.S)
        try:
            buffer = match.group(1).strip()
            response = self.clean_server_response(json.loads(buffer)['data'][0]
                )
        except SyntaxError as err:
            raise Exception('ill formatted response')
        else:
            return self.render_response(response, as_json)
    else:
        return None