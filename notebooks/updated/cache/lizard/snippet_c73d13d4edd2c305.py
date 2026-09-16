def edit(self):
    self.changed = False
    with self:
        editor = self.get_editor()
        cmd = [editor, self.name]
        try:
            res = subprocess.call(cmd)
        except Exception as e:
            print('Error launching editor %(editor)s' % locals())
            print(e)
            return
        if res != 0:
            msg = '%(editor)s returned error status %(res)d' % locals()
            raise EditProcessException(msg)
        new_data = self.read()
        if new_data != self.data:
            self.changed = self._save_diff(self.data, new_data)
            self.data = new_data