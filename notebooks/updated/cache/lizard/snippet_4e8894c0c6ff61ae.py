def _create_batch(signer, transactions):
    txn_ids = [txn.header_signature for txn in transactions]
    batch_header = BatchHeader(signer_public_key=signer.get_public_key().
        as_hex(), transaction_ids=txn_ids).SerializeToString()
    return Batch(header=batch_header, header_signature=signer.sign(
        batch_header), transactions=transactions)