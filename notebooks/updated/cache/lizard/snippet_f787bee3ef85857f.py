def legacy_tx(tx_ins, tx_outs, **kwargs):
    deser = [script_ser.deserialize(tx_in.redeem_script) for tx_in in
        tx_ins if tx_in.redeem_script is not None]
    version = max([guess_version(d) for d in deser])
    lock_time = max([guess_locktime(d) for d in deser])
    return tb.make_tx(version=version, tx_ins=tx_ins, tx_outs=tx_outs,
        lock_time=lock_time, tx_witnesses=None, expiry=kwargs['expiry'] if 
        'expiry' in kwargs else 0, tx_joinsplits=kwargs['tx_joinsplits'] if
        'tx_joinsplits' in kwargs else None, joinsplit_pubkey=kwargs[
        'joinsplit_pubkey'] if 'joinsplit_pubkey' in kwargs else None,
        joinsplit_sig=kwargs['joinsplit_sig'] if 'joinsplit_sig' in kwargs else
        None)