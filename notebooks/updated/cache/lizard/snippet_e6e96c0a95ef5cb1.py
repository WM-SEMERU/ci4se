def search_for_subject(self, subject, timeout=None, content_type=None):
    return self.search(timeout=timeout, content_type=content_type, SUBJECT=
        subject)