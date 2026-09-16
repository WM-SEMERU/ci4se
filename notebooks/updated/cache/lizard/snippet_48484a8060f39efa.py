def fetch_sender_txs(self):
    if len(self.sender_info.keys()) > 0:
        sender_txids = self.sender_info.keys()[:]
        sender_txid_batches = []
        batch_size = 20
        for i in xrange(0, len(sender_txids), batch_size):
            sender_txid_batches.append(sender_txids[i:i + batch_size])
        for i in xrange(0, len(sender_txid_batches)):
            sender_txid_batch = sender_txid_batches[i]
            log.debug('Fetch %s TXs via JSON-RPC (%s-%s of %s)' % (len(
                sender_txid_batch), i * batch_size, i * batch_size + len(
                sender_txid_batch), len(sender_txids)))
            sender_txs = None
            for j in xrange(0, 5):
                sender_txs = self.fetch_txs_rpc(self.bitcoind_opts,
                    sender_txid_batch)
                if sender_txs is None:
                    log.error(
                        'Failed to fetch transactions; trying again (%s of %s)'
                         % (j + 1, 5))
                    time.sleep(j + 1)
                    continue
                break
            if sender_txs is None:
                raise Exception('Failed to fetch transactions')
            for sender_txid, sender_tx in sender_txs.items():
                assert sender_txid in self.sender_info.keys(
                    ), 'Unsolicited sender tx %s' % sender_txid
                for nulldata_input_vout_index in self.sender_info[sender_txid
                    ].keys():
                    if (sender_txid !=
                        '0000000000000000000000000000000000000000000000000000000000000000'
                        ):
                        assert nulldata_input_vout_index < len(sender_tx[
                            'outs']
                            ), 'Output index {} is out of bounds for {}'.format(
                            nulldata_input_vout_index, sender_txid)
                        self.add_sender_info(sender_txid,
                            nulldata_input_vout_index, sender_tx['outs'][
                            nulldata_input_vout_index])
                    else:
                        self.add_sender_info(sender_txid,
                            nulldata_input_vout_index, sender_tx['outs'][0])
                self.num_txs_received += 1
    return True