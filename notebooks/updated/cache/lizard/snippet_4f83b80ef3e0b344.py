def _finalize_response(self, response):
    res = HttpResponse(content=response.content, content_type=self.
        _get_content_type())
    res.status_code = response.code
    return res