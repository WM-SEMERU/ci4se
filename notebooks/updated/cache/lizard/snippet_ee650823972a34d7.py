def of_text(self, text, encoding='utf-8'):
    m = self.hash_algo()
    m.update(text.encode(encoding))
    if self.return_int:
        return int(m.hexdigest(), 16)
    else:
        return m.hexdigest()