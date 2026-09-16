def applyAttributes(self, obj, attrs, codec=None):
    if not self._compiled:
        self.compile()
    if self.shortcut_decode:
        if self.is_dict:
            obj.update(attrs)
            return
        if not self.sealed:
            obj.__dict__.update(attrs)
            return
    else:
        attrs = self.getDecodableAttributes(obj, attrs, codec=codec)
    util.set_attrs(obj, attrs)