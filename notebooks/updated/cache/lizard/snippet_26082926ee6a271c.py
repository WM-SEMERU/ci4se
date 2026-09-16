def cli_guild(name, tibiadata, json):
    name = ' '.join(name)
    guild = _fetch_and_parse(Guild.get_url, Guild.from_content, Guild.
        get_url_tibiadata, Guild.from_tibiadata, tibiadata, name)
    if json and guild:
        print(guild.to_json(indent=2))
        return
    print(get_guild_string(guild))