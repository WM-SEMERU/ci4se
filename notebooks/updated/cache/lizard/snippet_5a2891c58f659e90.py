def get_int_id(self, str_id):
    if not str_id in self.mapping:
        if self.curr_id == IdRemapper.INT_MAX:
            return None
        self.mapping[str_id] = self.curr_id
        self.r_mapping[self.curr_id] = str_id
        self.curr_id += 1
    return self.mapping[str_id]