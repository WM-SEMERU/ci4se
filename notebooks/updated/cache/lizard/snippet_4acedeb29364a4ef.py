def titleize(word):
    return re.sub("\\b('?[a-z])", lambda match: match.group(1).capitalize(),
        humanize(underscore(word)))