def word(self):
    try:
        output = ensure_unicode(self.git.diff('--no-color',
            '--word-diff=plain', 'HEAD~1:content', 'HEAD:content').stdout)
    except sh.ErrorReturnCode_128:
        result = ensure_unicode(self.git.show('HEAD:content').stdout)
    else:
        ago = ensure_unicode(self.git.log('-2',
            '--pretty=format:last change was %cr', 'content').stdout
            ).splitlines()
        lines = output.splitlines()
        result = '\n'.join(itertools.chain(itertools.islice(itertools.
            dropwhile(lambda x: not x.startswith('@@'), lines[1:]), 1, None
            ), itertools.islice(ago, 1, None)))
    return result