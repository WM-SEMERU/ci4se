def sign_tx(network, tx, wifs=[], **kwargs):
    keychain = network.keychain()
    keychain.add_secrets(network.parse.wif(_) for _ in wifs)
    solver = tx.Solver(tx)
    solver.sign(keychain, **kwargs)