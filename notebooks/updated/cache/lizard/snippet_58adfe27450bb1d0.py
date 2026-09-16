def _process_counter_example(self, mma, w_string):
    w_string = self._find_bad_transition(mma, w_string)
    diff = len(w_string)
    same = 0
    while True:
        i = (same + diff) / 2
        access_string = self._run_in_hypothesis(mma, w_string, i)
        is_diff = self._check_suffix(w_string, access_string, i)
        if is_diff:
            diff = i
        else:
            same = i
        if diff - same == 1:
            break
    exp = w_string[diff:]
    self.observation_table.em_vector.append(exp)
    for row in (self.observation_table.sm_vector + self.observation_table.
        smi_vector):
        self._fill_table_entry(row, exp)