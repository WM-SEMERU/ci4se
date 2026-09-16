def set_range(self, start_index=0, end_index=None):
    if end_index is not None:
        end_index += 1
    self._test_list = StartEndList(start_index, end_index)
    self.session_info.start_index = start_index
    self.session_info.current_index = 0
    self.session_info.end_index = end_index
    self.session_info.test_list_str = self._test_list.as_test_list_str()
    return self