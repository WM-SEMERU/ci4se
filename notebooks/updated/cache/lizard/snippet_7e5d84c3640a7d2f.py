def run(self):
    self.input_channel.basic_consume(self.handle_message, queue=self.
        INPUT_QUEUE_NAME, no_ack=True)
    try:
        self.input_channel.start_consuming()
    except (KeyboardInterrupt, SystemExit):
        log.info(' Exiting')
        self.exit()