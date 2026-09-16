def _append(self, node, contents):
    if isinstance(contents, basestring):
        if contents != '':
            if len(node) == 0:
                if node.text is None:
                    node.text = contents
                else:
                    node.text += contents
            else:
                last = node[-1]
                if last.tail is None:
                    last.tail = contents
                else:
                    last.tail += contents
    elif et.iselement(contents):
        contents.tail = ''
        node.append(contents)
    else:
        try:
            for content in contents:
                self._append(node, content)
        except TypeError:
            self._append(node, self._format(contents))