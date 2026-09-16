def is_external(self):
    if self._P.Block.HintSystem == False:
        return True
    if self.is_luks_cleartext and self.luks_cleartext_slave.is_external:
        return True
    if self.is_partition and self.partition_slave.is_external:
        return True
    return False