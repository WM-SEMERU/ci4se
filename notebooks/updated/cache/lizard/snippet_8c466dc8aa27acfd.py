def method_name(self):
    if isinstance(self.view_func, str):
        return self.view_func
    return self.view_func.__name__