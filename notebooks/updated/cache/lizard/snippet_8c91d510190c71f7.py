def from_string(cls, raw_filter, rule_limit):
    parsed_filter = cls.replace_tags(raw_filter)
    regexes = cls.build_regex_list(parsed_filter, rule_limit)
    return cls(regexes)