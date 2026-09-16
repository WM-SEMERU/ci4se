def get_rules_from_disk():
    my_dir = os.path.dirname(os.path.realpath(__file__))
    yara_rule_path = os.path.join(my_dir, 'yara/rules')
    if not os.path.exists(yara_rule_path):
        raise RuntimeError(
            'yara could not find yara rules directory under: %s' % my_dir)
    rules = yara.load_rules(rules_rootpath=yara_rule_path, fast_match=True)
    return rules