def load(obj, env=None, silent=True, key=None):
    redis = StrictRedis(**obj.get('REDIS_FOR_DYNACONF'))
    holder = obj.get('ENVVAR_PREFIX_FOR_DYNACONF')
    try:
        if key:
            value = redis.hget(holder.upper(), key)
            if value:
                obj.logger.debug('redis_loader: loading by key: %s:%s (%s:%s)',
                    key, value, IDENTIFIER, holder)
            if value:
                parsed_value = parse_conf_data(value, tomlfy=True)
                if parsed_value:
                    obj.set(key, parsed_value)
        else:
            data = {key: parse_conf_data(value, tomlfy=True) for key, value in
                redis.hgetall(holder.upper()).items()}
            if data:
                obj.logger.debug('redis_loader: loading: %s (%s:%s)', data,
                    IDENTIFIER, holder)
                obj.update(data, loader_identifier=IDENTIFIER)
    except Exception as e:
        if silent:
            if hasattr(obj, 'logger'):
                obj.logger.error(str(e))
            return False
        raise