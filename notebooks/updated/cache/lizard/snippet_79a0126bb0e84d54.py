def save_token(self, token, request, *args, **kwargs):
    return self.save_bearer_token(token, request, *args, **kwargs)