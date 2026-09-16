def settlements(ctx, asset, limit):
    from bitshares.asset import Asset
    asset = Asset(asset, full=True)
    if not asset.is_bitasset:
        print_message('{} is not a bitasset.'.format(asset['symbol']),
            'warning')
        sys.exit(1)
    calls = asset.get_settle_orders(limit)
    t = [['acount', 'amount', 'date']]
    for call in calls:
        t.append([str(call['account']['name']), str(call['amount']), str(
            call['date'])])
    print_table(t)