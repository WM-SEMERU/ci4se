def _handle_ctrl_c(self, *args):
    if self.anybar:
        self.anybar.change('exclamation')
    if self._stop:
        print('\nForced shutdown...')
        raise SystemExit
    if not self._stop:
        hline = 42 * '='
        print('\n' + hline +
            """
Got CTRL+C, waiting for current cycle...
Press CTRL+C again if you're in hurry!
"""
             + hline)
        self._stop = True