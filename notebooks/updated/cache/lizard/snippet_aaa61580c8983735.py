def failure_count(self):
    return len([i for i, result in enumerate(self.data) if result.failure])