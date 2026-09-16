def stop_and_persist(self, symbol=' ', text=None):
    if not self._enabled:
        return self
    symbol = decode_utf_8_text(symbol)
    if text is not None:
        text = decode_utf_8_text(text)
    else:
        text = self._text['original']
    text = text.strip()
    if self._text_color:
        text = colored_frame(text, self._text_color)
    self.stop()
    output = '{0} {1}\n'.format(*[(text, symbol) if self._placement ==
        'right' else (symbol, text)][0])
    try:
        self._stream.write(output)
    except UnicodeEncodeError:
        self._stream.write(encode_utf_8_text(output))
    return self