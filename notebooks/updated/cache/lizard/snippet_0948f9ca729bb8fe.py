def _process_req_body(self, body):
    try:
        return json.loads(body)
    except ValueError:
        return urlparse.parse_qs(body, keep_blank_values=True)