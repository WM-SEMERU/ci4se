def get_last_rate_limit_info(self, action, method):
    method = method.upper()
    if (action in self.last_rate_limit_info and method in self.
        last_rate_limit_info[action]):
        return self.last_rate_limit_info[action][method]
    return None