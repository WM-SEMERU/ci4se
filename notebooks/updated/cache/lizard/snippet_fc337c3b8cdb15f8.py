def _doit(self):
    while len(self._truisms):
        truism = self._truisms.pop()
        if truism in self._processed_truisms:
            continue
        unpacked_truisms = self._unpack_truisms(truism)
        self._processed_truisms.add(truism)
        if len(unpacked_truisms):
            self._queue_truisms(unpacked_truisms, check_true=True)
            continue
        if not self._handleable_truism(truism):
            continue
        truism = self._adjust_truism(truism)
        assumptions = self._get_assumptions(truism)
        if truism not in self._identified_assumptions and len(assumptions):
            l.debug('Queued assumptions %s for truism %s.', assumptions, truism
                )
            self._truisms.extend(assumptions)
            self._identified_assumptions.update(assumptions)
        l.debug('Processing truism %s', truism)
        balanced_truism = self._balance(truism)
        l.debug('... handling')
        self._handle(balanced_truism)