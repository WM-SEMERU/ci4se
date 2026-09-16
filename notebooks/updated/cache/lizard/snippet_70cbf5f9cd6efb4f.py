def post_submission(self):
    name = self.content.name
    if '+' in name or name in ('/r/all', '/r/front', '/r/me', '/u/saved'):
        self.term.show_notification("Can't post to {0}".format(name))
        return
    submission_info = docs.SUBMISSION_FILE.format(name=name)
    with self.term.open_editor(submission_info) as text:
        if not text:
            self.term.show_notification('Canceled')
            return
        elif '\n' not in text:
            self.term.show_notification('Missing body')
            return
        title, content = text.split('\n', 1)
        with self.term.loader('Posting', delay=0):
            submission = self.reddit.submit(name, title, text=content,
                raise_captcha_exception=True)
            time.sleep(2.0)
        if self.term.loader.exception:
            raise TemporaryFileError()
    if not self.term.loader.exception:
        self.selected_page = self.open_submission_page(submission=submission)