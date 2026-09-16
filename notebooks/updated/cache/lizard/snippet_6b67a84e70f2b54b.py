def cdbs(client, event, channel, nick, rest):
    db_name, shard = shlex.split(rest)
    return sharding.create_db_in_shard(db_name, shard, client=get_client())