def _render_val_with_prev(self, w, n, current_val, symbol_len):
    sl = symbol_len - 1
    if len(w) > 1:
        out = self._revstart
        if current_val != self.prior_val:
            out += self._x + hex(current_val).rstrip('L').ljust(sl)[:sl]
        elif n == 0:
            out += hex(current_val).rstrip('L').ljust(symbol_len)[:symbol_len]
        else:
            out += ' ' * symbol_len
        out += self._revstop
    else:
        pretty_map = {(0, 0): self._low + self._low * sl, (0, 1): self._up +
            self._high * sl, (1, 0): self._down + self._low * sl, (1, 1): 
            self._high + self._high * sl}
        out = pretty_map[self.prior_val, current_val]
    return out