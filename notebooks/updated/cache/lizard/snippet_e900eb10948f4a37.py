def process_boolean_array(self, tag):
    array_size = tag.get_array_size()
    tag.set_address(self.normal_register.get_array(array_size))
    if self.is_sixteen_bit:
        self.normal_register.move_to_next_address(array_size / 16 + 1)
        return
    self.normal_register.move_to_next_address(array_size / 8 + 1)