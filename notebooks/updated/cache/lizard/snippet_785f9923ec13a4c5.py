def load_pa11y_results(stdout, spider, url):
    if not stdout:
        return []
    results = json.loads(stdout.decode('utf8'))
    ignore_rules = ignore_rules_for_url(spider, url)
    for rule in ignore_rules:
        results = [result for result in results if not
            ignore_rule_matches_result(rule, result)]
    return results