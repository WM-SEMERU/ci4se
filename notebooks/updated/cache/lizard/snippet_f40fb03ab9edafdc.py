def do_rm(self, subcmd, opts, message):
    maildir = self.maildir
    client = MdClient(maildir, filesystem=self.filesystem)
    try:
        client.remove(message)
    except KeyError:
        return 1