def get_command_response_from_cache(self, device_id, command, command2):
    key = self.create_key_from_command(command, command2)
    command_cache = self.get_cache_from_file(device_id)
    if device_id not in command_cache:
        command_cache[device_id] = {}
        return False
    elif key not in command_cache[device_id]:
        return False
    response = command_cache[device_id][key]
    expired = False
    if response['ttl'] < int(time()):
        self.logger.info('cache expired for device %s', device_id)
        expired = True
        if os.path.exists(LOCK_FILE):
            self.logger.info('cache locked - will wait to rebuild %s',
                device_id)
        else:
            self.logger.info('cache unlocked - will rebuild %s', device_id)
            newpid = os.fork()
            if newpid == 0:
                self.rebuild_cache(device_id, command, command2)
    if expired:
        self.logger.info('returning expired cached device status %s', device_id
            )
    else:
        self.logger.info('returning unexpired cached device status %s',
            device_id)
    return response['response']