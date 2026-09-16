def find_word_groups(string, words):
    scale_pattern = '|'.join(words)
    regex = re.compile('(?:(?:\\d+)\\s+(?:' + scale_pattern +
        ')*\\s*)+(?:\\d+|' + scale_pattern + ')+')
    result = regex.findall(string)
    return result