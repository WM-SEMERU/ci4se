def set_text(self, text):
    if text in [None, '']:
        return self.jsonrpc.clearTextField(self.selector)
    else:
        return self.jsonrpc.setText(self.selector, text)