def rulefiles(self, acc=None):
    rulesdir = self.rulesdir(acc)
    rules = [os.path.join(rulesdir, x) for x in self.get('rules', acc, [])]
    if acc is not None:
        rules += self.rulefiles(acc=None)
    return rules