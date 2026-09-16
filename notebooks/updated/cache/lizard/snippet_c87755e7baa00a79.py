def _validate(self, writing=False):
    if len(self.bits_per_component) != len(self.signed) or len(self.signed
        ) != self.palette.shape[1]:
        msg = (
            "The length of the 'bits_per_component' and the 'signed' members must equal the number of columns of the palette."
            )
        self._dispatch_validation_error(msg, writing=writing)
    bps = self.bits_per_component
    if writing and not all(b == bps[0] for b in bps):
        msg = 'Writing palettes with varying bit depths is not supported.'
        self._dispatch_validation_error(msg, writing=writing)