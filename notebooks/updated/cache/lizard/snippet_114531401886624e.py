def _reflex_rule_process(self, wf_action):
    a_method = self.getMethod()
    if not a_method:
        return
    all_rrs = a_method.getBackReferences('ReflexRuleMethod')
    if not all_rrs:
        return
    for rule in all_rrs:
        if not api.is_active(rule):
            continue
        action_row = rule.getActionReflexRules(self, wf_action)
        doReflexRuleAction(self, action_row)