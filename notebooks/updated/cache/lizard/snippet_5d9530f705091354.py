def update(tgt, tgt_type='glob', clear=False, mine_functions=None):
    ret = __salt__['salt.execute'](tgt, 'mine.update', tgt_type=tgt_type,
        clear=clear, mine_functions=mine_functions)
    return ret