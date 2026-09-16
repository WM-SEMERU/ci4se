def maybeUpdate(self):
    if self.wasModified():
        self.lastModified = self.filePath.getmtime()
        self.fileContents = self.filePath.getContent()
        self.hashValue = hashlib.sha1(self.fileContents).hexdigest()