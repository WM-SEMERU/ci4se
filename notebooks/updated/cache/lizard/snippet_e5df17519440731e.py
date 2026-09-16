def randomwif(prefix, num):
    from bitsharesbase.account import PrivateKey
    t = [['wif', 'pubkey']]
    for n in range(0, num):
        wif = PrivateKey()
        t.append([str(wif), format(wif.pubkey, prefix)])
    print_table(t)