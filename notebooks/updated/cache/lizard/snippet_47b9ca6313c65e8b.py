def invalid_content_type(self, request=None, response=None):
    if callable(self.invalid_outputs.content_type):
        return self.invalid_outputs.content_type(request=request, response=
            response)
    else:
        return self.invalid_outputs.content_type