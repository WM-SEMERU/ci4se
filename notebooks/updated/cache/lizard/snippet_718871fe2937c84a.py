def update_contents(self, contents, mime_type):
    import hashlib
    import time
    new_size = len(contents)
    self.mime_type = mime_type
    if mime_type == 'text/plain':
        self.contents = contents.encode('utf-8')
    else:
        self.contents = contents
    old_hash = self.hash
    self.hash = hashlib.md5(self.contents).hexdigest()
    if self.size and old_hash != self.hash:
        self.modified = int(time.time())
    self.size = new_size