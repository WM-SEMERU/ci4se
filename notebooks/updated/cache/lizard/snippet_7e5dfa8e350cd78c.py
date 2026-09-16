def syllable_split(string):
    p = "\\'[%s]+|`[%s]+|[%s]+|[^%s\\'`\\.]+|[^\\.]{1}" % (A, A, A, A)
    return re.findall(p, string, flags=FLAGS)