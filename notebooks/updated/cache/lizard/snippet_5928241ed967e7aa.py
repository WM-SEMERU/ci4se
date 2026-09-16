def distribute_from_split_pool(tx, fee):
    if fee == 'standard':
        fee = tx_fee.recommended_fee_for_tx(tx)
    zero_txs_out = [tx_out for tx_out in tx.txs_out if tx_out.coin_value == 0]
    zero_count = len(zero_txs_out)
    if zero_count > 0:
        total_coin_value = sum(spendable.coin_value for spendable in tx.
            unspents)
        coins_allocated = sum(tx_out.coin_value for tx_out in tx.txs_out) + fee
        remaining_coins = total_coin_value - coins_allocated
        if remaining_coins < 0:
            raise ValueError('insufficient inputs for outputs')
        if remaining_coins < zero_count:
            raise ValueError(
                'not enough to pay nonzero amounts to at least one of the unspecified outputs'
                )
        for value, tx_out in zip(split_with_remainder(remaining_coins,
            zero_count), zero_txs_out):
            tx_out.coin_value = value
    return zero_count