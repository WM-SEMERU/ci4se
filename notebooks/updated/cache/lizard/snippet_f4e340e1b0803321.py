def pending_transactions(server):
    namecoind = NamecoindClient(server, NAMECOIND_PORT, NAMECOIND_USER,
        NAMECOIND_PASSWD)
    reply = namecoind.listtransactions('', 10000)
    counter = 0
    for i in reply:
        if i['confirmations'] == 0:
            counter += 1
    return counter