def get_tokens(self, node, include_extra=False):
    return self.token_range(node.first_token, node.last_token,
        include_extra=include_extra)