def FUNCTIONNOPROTO(self, _cursor_type):
    returns = _cursor_type.get_result()
    returns = self.parse_cursor_type(returns)
    attributes = []
    obj = typedesc.FunctionType(returns, attributes)
    self.set_location(obj, None)
    return obj