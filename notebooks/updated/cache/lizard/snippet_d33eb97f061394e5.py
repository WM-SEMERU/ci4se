def run(self, matches):

    def _run(matches):
        group_starting_pos = 0
        for current_pos, (group_length, group_function) in enumerate(zip(
            self.group_lengths, self.group_functions)):
            start_pos = current_pos + group_starting_pos
            end_pos = current_pos + group_starting_pos + group_length
            yield group_function(matches[start_pos:end_pos])
            group_starting_pos += group_length - 1
    return self.final_function(list(_run(matches)))