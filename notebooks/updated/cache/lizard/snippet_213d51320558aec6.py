def set_screen(self, screen, overwrite=False):
    if self._screen is not None and not overwrite:
        raise ValueError(
            """set_screen() called with overwrite=False and screen already set.
If you want to apply multiple filters as a screen use set_screen(filter1 & filter2 & ...).
If you want to replace the previous screen with a new one, use set_screen(new_filter, overwrite=True)."""
            )
    self._screen = screen