def issue(self, test, err):
    self.step.setProgress('tests failed', len(self.failures) + len(self.errors)
        )