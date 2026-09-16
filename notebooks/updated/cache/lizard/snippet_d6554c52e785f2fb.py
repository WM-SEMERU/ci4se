def is_email_address(string):
    return string and isinstance(string, base_string
        ) and REGEX_PATTERN_EMAIL_ADDRESS.match(string.strip().lower())