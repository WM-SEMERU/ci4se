def _load_score(self):
    score = int(self.score_file.read())
    self.score_file.seek(0, os.SEEK_SET)
    return score