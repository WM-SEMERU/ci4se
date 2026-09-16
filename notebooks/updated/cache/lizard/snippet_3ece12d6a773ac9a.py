def available_players():
    bus = dbus.SessionBus()
    players = set()
    for name in filter(lambda item: item.startswith(MPRIS_NAME_PREFIX), bus
        .list_names()):
        owner_name = bus.get_name_owner(name)
        players.add(convert(owner_name))
    return players