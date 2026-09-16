def blank_account(cls, db, addr, initial_nonce=0):
    db.put(BLANK_HASH, b'')
    o = cls(initial_nonce, 0, trie.BLANK_ROOT, BLANK_HASH, db, addr)
    o.existent_at_start = False
    return o