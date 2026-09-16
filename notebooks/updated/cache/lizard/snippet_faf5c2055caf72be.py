def history(self, hash):
    txs = self._t.get(hash, max_transactions=10000)['transactions']
    tree = defaultdict(list)
    number_editions = 0
    for tx in txs:
        _tx = self._t.get(tx['txid'])
        txid = _tx['txid']
        verb_str = BlockchainSpider.check_script(_tx['vouts'])
        verb = Spoolverb.from_verb(verb_str)
        from_address, to_address, piece_address = (BlockchainSpider.
            _get_addresses(_tx))
        timestamp_utc = _tx['time']
        action = verb.action
        edition_number = 0
        if action != 'EDITIONS':
            edition_number = verb.edition_number
        else:
            number_editions = verb.num_editions
        tree[edition_number].append({'txid': txid, 'verb': verb_str,
            'from_address': from_address, 'to_address': to_address,
            'piece_address': piece_address, 'timestamp_utc': timestamp_utc,
            'action': action, 'number_editions': number_editions,
            'edition_number': edition_number})
    for edition, chain in tree.items():
        [d.update({'number_editions': number_editions}) for d in chain]
    return dict(tree)