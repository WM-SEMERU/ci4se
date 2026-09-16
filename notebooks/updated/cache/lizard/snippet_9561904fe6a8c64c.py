def select_inputs(self, address, nfees, ntokens, min_confirmations=6):
    unspents = self._t.get(address, min_confirmations=min_confirmations)[
        'unspents']
    unspents = [u for u in unspents if u not in self._spents.queue]
    if len(unspents) == 0:
        raise Exception('No spendable outputs found')
    fees = [u for u in unspents if u['amount'] == self.fee][:nfees]
    tokens = [u for u in unspents if u['amount'] == self.token][:ntokens]
    if len(fees) != nfees or len(tokens) != ntokens:
        raise SpoolFundsError('Not enough outputs to spend. Refill your wallet'
            )
    if self._spents.qsize() > self.SPENTS_QUEUE_MAXSIZE - (nfees + ntokens):
        [self._spents.get() for i in range(self._spents.qsize() + nfees +
            ntokens - self.SPENTS_QUEUE_MAXSIZE)]
    [self._spents.put(fee) for fee in fees]
    [self._spents.put(token) for token in tokens]
    return fees + tokens