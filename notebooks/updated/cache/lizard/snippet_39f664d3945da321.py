def _apply_rate(self, max_rate, aggressive=False):
    self.log('Called _apply_rate')
    self.log(['  Aggressive: %s', aggressive])
    self.log(['  Max rate:   %.3f', max_rate])
    regular_fragments = list(self.smflist.regular_fragments)
    if len(regular_fragments) <= 1:
        self.log('  The list contains at most one regular fragment, returning')
        return
    faster_fragments = [(i, f) for i, f in regular_fragments if f.rate is not
        None and f.rate >= max_rate + Decimal('0.001')]
    if len(faster_fragments) == 0:
        self.log('  No regular fragment faster than max rate, returning')
        return
    self.log_warn('  Some fragments have rate faster than max rate:')
    self.log(['  %s', [i for i, f in faster_fragments]])
    self.log('Fixing rate for faster fragments...')
    for frag_index, fragment in faster_fragments:
        self.smflist.fix_fragment_rate(frag_index, max_rate, aggressive=
            aggressive)
    self.log('Fixing rate for faster fragments... done')
    faster_fragments = [(i, f) for i, f in regular_fragments if f.rate is not
        None and f.rate >= max_rate + Decimal('0.001')]
    if len(faster_fragments) > 0:
        self.log_warn('  Some fragments still have rate faster than max rate:')
        self.log(['  %s', [i for i, f in faster_fragments]])