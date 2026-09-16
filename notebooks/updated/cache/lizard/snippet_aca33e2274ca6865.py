def zavg(self, name, score_start, score_end):
    score_start = get_integer_or_emptystring('score_start', score_start)
    score_end = get_integer_or_emptystring('score_end', score_end)
    return self.execute_command('zavg', name, score_start, score_end)