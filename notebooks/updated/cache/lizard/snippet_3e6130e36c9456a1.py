def _HashBlock(self, block, start, end):
    for finger in self.fingers:
        expected_range = finger.CurrentRange()
        if expected_range is None:
            continue
        if (start > expected_range.start or start == expected_range.start and
            end > expected_range.end or start < expected_range.start and 
            end > expected_range.start):
            raise RuntimeError('Cutting across fingers.')
        if start == expected_range.start:
            finger.HashBlock(block)