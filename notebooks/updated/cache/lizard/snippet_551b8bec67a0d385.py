def _action_set_subsumption(self, action_set):
    selected_rule = None
    selected_bit_count = None
    for rule in action_set:
        if not (rule.experience > self.subsumption_threshold and rule.error <
            self.error_threshold):
            continue
        bit_count = rule.condition.count()
        if (selected_rule is None or bit_count > selected_bit_count or 
            bit_count == selected_bit_count and random.randrange(2)):
            selected_rule = rule
            selected_bit_count = bit_count
    if selected_rule is None:
        return
    to_remove = []
    for rule in action_set:
        if selected_rule is not rule and selected_rule.condition(rule.condition
            ):
            selected_rule.numerosity += rule.numerosity
            action_set.model.discard(rule, rule.numerosity)
            to_remove.append(rule)
    for rule in to_remove:
        action_set.remove(rule)