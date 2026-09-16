def order_descending(self):
    self._query.append('ORDERBYDESC{0}'.format(self.current_field))
    self.c_oper = inspect.currentframe().f_back.f_code.co_name
    return self