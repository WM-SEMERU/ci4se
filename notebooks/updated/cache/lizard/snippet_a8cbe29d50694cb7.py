def flatten_rules(self, declarations):
    rules = []
    for protocole, paths in declarations:
        if protocole:
            continue
        rules.extend([self.strip_quotes(v.strip()) for v in paths.split(',')])
    return list(filter(self.filter_rules, rules))