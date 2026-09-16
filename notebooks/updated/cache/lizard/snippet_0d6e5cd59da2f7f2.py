def delete(self, *args):
    key = self.name_wid.text or self.name_wid.hint_text
    if not hasattr(self.store, key):
        return
    delattr(self.store, key)
    try:
        return min(kee for kee in dir(self.store) if kee > key)
    except ValueError:
        return '+'