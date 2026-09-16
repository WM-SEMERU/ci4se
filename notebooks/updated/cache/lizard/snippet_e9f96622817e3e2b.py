def split_into_sentences(s):
    s = re.sub('\\s+', ' ', s)
    s = re.sub('[\\\\.\\\\?\\\\!]', '\n', s)
    return s.split('\n')