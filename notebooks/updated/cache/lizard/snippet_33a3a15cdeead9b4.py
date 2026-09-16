def build_sha1(self):
    if len(self.dutinformation) > 0 and self.dutinformation.get(0
        ).build is not None:
        return self.dutinformation.get(0).build.sha1
    return None