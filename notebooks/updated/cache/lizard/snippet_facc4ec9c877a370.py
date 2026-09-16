def _match_magic(self, full_path):
    for magic in self.magics:
        if magic.matches(full_path):
            return magic