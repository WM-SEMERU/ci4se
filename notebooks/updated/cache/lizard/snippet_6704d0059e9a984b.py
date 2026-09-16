def access_token(self, cookie):
    if cookie:
        token = self._generate_random_string(self.access_tokens)
        self.access_tokens[token] = cookie, int(time.time())
        return token
    else:
        return None