def move_down(self):
    old_index = self.current_index
    self.current_index += 1
    self.__wrap_index()
    self.__handle_selections(old_index, self.current_index)