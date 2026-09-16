def get_email_regex(self):
    validator = self.default_validators[0]
    user_regex = validator.user_regex.pattern.replace('\\Z', '@')
    domain_patterns = [(re.escape(domain) + '$') for domain in validator.
        domain_whitelist] + [validator.domain_regex.pattern.replace('\\Z', '$')
        ]
    domain_regex = '({0})'.format('|'.join(domain_patterns))
    email_regex = user_regex + domain_regex
    return re.sub('\\(\\?\\<[^()]*?\\)', '', email_regex)