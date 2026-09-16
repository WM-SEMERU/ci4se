def run(self, node, client):
    perms = os.stat(self.source).st_mode
    client.put(path=self.target, chmod=perms, contents=open(self.source,
        'rb').read())
    return node