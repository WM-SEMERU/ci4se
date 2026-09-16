def hash(ctx, message_id, message):
    conf = Config(message_id=message_id)
    mail = Mail(message, conf)
    logger.info(mail.header_text)
    logger.info('-' * 70)
    logger.info('Hash: {}'.format(mail.hash_key))