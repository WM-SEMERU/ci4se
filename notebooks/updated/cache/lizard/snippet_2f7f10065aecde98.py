def add_match_rules(self, match_rules):
    if type(match_rules) == list:
        for r in match_rules:
            self.add_match_rule(r)
    else:
        self.add_match_rule(match_rules)