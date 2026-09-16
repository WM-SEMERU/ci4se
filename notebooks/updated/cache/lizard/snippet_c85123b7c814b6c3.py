def add_lifecycle_delete_rule(self, **kw):
    rules = list(self.lifecycle_rules)
    rules.append(LifecycleRuleDelete(**kw))
    self.lifecycle_rules = rules