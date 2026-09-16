def post(self, endpoint, return_response=False, **kwargs):
    args = self.translate_kwargs(**kwargs)
    response = self.session.post(self.make_url(endpoint), **args)
    decoded_response = _decode_response(response)
    if return_response:
        return decoded_response, response
    return decoded_response