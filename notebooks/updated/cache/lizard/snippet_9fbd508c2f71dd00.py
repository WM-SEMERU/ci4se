def sub_notes(docs):

    def substitute(match):
        ret = (
            '</p><div class="alert alert-{}" role="alert"><h4>{}</h4><p>{}</p></div>'
            .format(NOTE_TYPE[match.group(1).lower()], match.group(1).
            capitalize(), match.group(2)))
        if len(match.groups()) >= 4 and not match.group(4):
            ret += '\n<p>'
        return ret
    for regex in NOTE_RE:
        docs = regex.sub(substitute, docs)
    return docs