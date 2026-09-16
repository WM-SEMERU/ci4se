def insert_completion(self, p_insert):
    start, end = self._surrounding_text
    final_text = start + p_insert + end
    self.set_edit_text(final_text)
    self.set_edit_pos(len(start) + len(p_insert))