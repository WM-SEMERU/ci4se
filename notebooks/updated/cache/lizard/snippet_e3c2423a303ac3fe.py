def transaction(self, compare, success=None, failure=None):
    compare = [c.build_message() for c in compare]
    success_ops = self._ops_to_requests(success)
    failure_ops = self._ops_to_requests(failure)
    transaction_request = etcdrpc.TxnRequest(compare=compare, success=
        success_ops, failure=failure_ops)
    txn_response = self.kvstub.Txn(transaction_request, self.timeout,
        credentials=self.call_credentials, metadata=self.metadata)
    responses = []
    for response in txn_response.responses:
        response_type = response.WhichOneof('response')
        if response_type in ['response_put', 'response_delete_range',
            'response_txn']:
            responses.append(response)
        elif response_type == 'response_range':
            range_kvs = []
            for kv in response.response_range.kvs:
                range_kvs.append((kv.value, KVMetadata(kv, txn_response.
                    header)))
            responses.append(range_kvs)
    return txn_response.succeeded, responses