def parse_parameters_from_response(self, response):
    lines = response.splitlines()
    pairs = [line.strip().split('=', 1) for line in lines if '=' in line]
    pairs = sorted(pairs)
    signature = ([unquote(v) for k, v in pairs if k == 'h'] or [None])[0]
    query_string = '&'.join([(k + '=' + v) for k, v in pairs if k != 'h'])
    return signature, query_string