def filter_completions(self, completions):
    completions = [ensure_str(c) for c in completions]
    if self.exclude is None:
        self.exclude = set()
    seen = set(self.exclude)
    return [c for c in completions if c not in seen and not seen.add(c)]