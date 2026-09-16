def notice(self, client, message):
    if client and message:
        messages = utils.split_message(message, self.config.max_length)
        for msg in messages:
            client.fwrite(':{c.srv} NOTICE {c.nick} :{msg}', msg=msg)