def _verify_primary(self, new_primary, ledger_info):
    expected_primary = self.provider.next_primary_name()
    if new_primary != expected_primary:
        logger.error(
            '{}{} expected next primary to be {}, but majority declared {} instead for view {}'
            .format(PRIMARY_SELECTION_PREFIX, self.name, expected_primary,
            new_primary, self.view_no))
        return False
    self._primary_verified = True
    return True