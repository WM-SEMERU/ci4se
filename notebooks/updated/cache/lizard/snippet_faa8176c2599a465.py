def get_last_offset(self, field, filters_=[]):
    offset = self.get_last_item_field(field, filters_=filters_, offset=True)
    return offset