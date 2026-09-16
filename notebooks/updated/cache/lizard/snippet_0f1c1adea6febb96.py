def comment(self, text, comment_prefix='#'):
    comment = Comment(self._container)
    if not text.startswith(comment_prefix):
        text = '{} {}'.format(comment_prefix, text)
    if not text.endswith('\n'):
        text = '{}{}'.format(text, '\n')
    comment.add_line(text)
    self._container.structure.insert(self._idx, comment)
    self._idx += 1
    return self