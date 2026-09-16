def error(self, message):
    if ('not allowed' in message or 'ignored' in message or 'expected' in
        message or 'invalid' in message or self.add_help):
        super(IntermediateConfigmanParser, self).error(message)