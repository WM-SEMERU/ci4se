def create_token_review(self, body, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.create_token_review_with_http_info(body, **kwargs)
    else:
        data = self.create_token_review_with_http_info(body, **kwargs)
        return data