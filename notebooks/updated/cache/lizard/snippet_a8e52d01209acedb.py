def parse(self, string, root=None):
    phrases = []
    meta = self.meta.search(string)
    while meta:
        pos = meta.start()
        if meta.group() == '<':
            string, child, meta = self.open_phrase(string, pos)
            if child and root:
                root.nested.append(child)
            elif child:
                phrases.append(child)
            continue
        elif root:
            if meta.group() == '(':
                meta = self.meta.search(string, pos + 1)
                if meta.group() == ')':
                    string, root, meta = self.handle_arguments(string, root,
                        pos, meta.start())
                    continue
            elif meta.group() == '>':
                string, phrase, meta = self.close_phrase(string, root, pos)
                if phrase:
                    return string, phrase
                continue
        string, meta = self.escape_meta(string, pos)
    if not root:
        return string, phrases
    word = re.search('([\\w\\s]+)(?![\\d]*>[\\w\\s]+>)', string)
    what = 'No closing tag found for opening tag'
    if word:
        what += " after expression '{0}'".format(word.group())
    raise errors.ParseError(what + '!')