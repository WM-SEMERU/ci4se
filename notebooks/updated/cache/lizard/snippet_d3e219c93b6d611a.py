def build_rules(rule_yaml, match_plugins, action_plugins):
    rule_sets = []
    for yaml_section in rule_yaml:
        rule_sets.append(RuleSet(yaml_section, match_plugins=match_plugins,
            action_plugins=action_plugins))
    return rule_sets