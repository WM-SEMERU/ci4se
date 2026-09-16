def run(self):
    self._unlock_keychain()
    item = self.keychain.item(self.arguments.item, fuzzy_threshold=self.
        _fuzzy_threshold())
    if item is not None:
        self.stdout.write('%s\n' % item.password)
    else:
        self.stderr.write("1pass: Could not find an item named '%s'\n" % (
            self.arguments.item,))
        sys.exit(os.EX_DATAERR)