def receive_reply(self, msg, content):
    reply_head = content.head()
    if reply_head == 'error':
        comment = content.gets('comment')
        logger.error('Got error reply: "%s"' % comment)
    else:
        extractions = content.gets('ekb')
        self.extractions.append(extractions)
    self.reply_counter -= 1
    if self.reply_counter == 0:
        self.exit(0)