def whitelist(ctx, whitelist_account, account):
    account = Account(account, blockchain_instance=ctx.blockchain)
    print_tx(account.whitelist(whitelist_account))