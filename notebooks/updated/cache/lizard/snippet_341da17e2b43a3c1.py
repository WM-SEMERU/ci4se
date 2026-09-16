def _apply_commit_rules(rules, commit):
    all_violations = []
    for rule in rules:
        violations = rule.validate(commit)
        if violations:
            all_violations.extend(violations)
    return all_violations