def get_cards_stats(ctx, currency, skip_owned, appid, foil):
    username = ctx.obj['username']
    cards_by_app = defaultdict(list)
    inventory = User(username).traverse_inventory(item_filter=
        TAG_ITEM_CLASS_CARD)
    for item in inventory:
        appid_ = item.app.appid
        if not appid or appid_ in appid:
            cards_by_app[appid_].append(item)
    if not cards_by_app:
        click.secho('User `%s` has no cards' % username, fg='red', err=True)
        return
    for appid_, cards in cards_by_app.items():
        app = cards[0].app
        print_card_prices(app.appid, currency, owned_cards=[card.title for
            card in cards], skip_owned=skip_owned, foil=foil)