def create_self_subject_access_review(self, body, **kwargs):
    kwargs['_return_http_data_only'] = True
    if kwargs.get('async_req'):
        return self.create_self_subject_access_review_with_http_info(body,
            **kwargs)
    else:
        data = self.create_self_subject_access_review_with_http_info(body,
            **kwargs)
        return data