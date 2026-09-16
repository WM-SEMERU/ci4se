def process_messages(self):
    try:
        msg = self.msgbackend.pop(self.incoming_message_mailbox)
        self.handle_incoming_message(msg)
    except queue.Empty:
        logger.debug('Worker message queue currently empty.')