def indian_punctuation_tokenize_regex(self, untokenized_string: str):
    modified_punctuations = string.punctuation.replace('|', '')
    indian_punctuation_pattern = re.compile('([' + modified_punctuations +
        '।॥' + ']|\\|+)')
    tok_str = indian_punctuation_pattern.sub(' \\1 ', untokenized_string.
        replace('\t', ' '))
    return re.sub('[ ]+', ' ', tok_str).strip(' ').split(' ')