def _should_remove(self, i, name):
    if self.params[i].showkey:
        following = self.params[i + 1:]
        better_matches = [(after.name.strip() == name and not after.showkey
            ) for after in following]
        return any(better_matches)
    return False