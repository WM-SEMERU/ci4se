def send_all():
    EMAIL_BACKEND = getattr(settings, 'MAILER_EMAIL_BACKEND',
        'django.core.mail.backends.smtp.EmailBackend')
    acquired, lock = acquire_lock()
    if not acquired:
        return
    start_time = time.time()
    deferred = 0
    sent = 0
    try:
        connection = None
        for message in prioritize():
            try:
                if connection is None:
                    connection = get_connection(backend=EMAIL_BACKEND)
                logging.info("sending message '{0}' to {1}".format(message.
                    subject, ', '.join(message.to_addresses)))
                email = message.email
                if email is not None:
                    email.connection = connection
                    if not hasattr(email, 'reply_to'):
                        email.reply_to = []
                    ensure_message_id(email)
                    email.send()
                    email.connection = None
                    message.email = email
                    MessageLog.objects.log(message, RESULT_SUCCESS)
                    sent += 1
                else:
                    logging.warning(
                        "message discarded due to failure in converting from DB. Added on '%s' with priority '%s'"
                         % (message.when_added, message.priority))
                message.delete()
            except (socket_error, smtplib.SMTPSenderRefused, smtplib.
                SMTPRecipientsRefused, smtplib.SMTPDataError, smtplib.
                SMTPAuthenticationError) as err:
                message.defer()
                logging.info('message deferred due to failure: %s' % err)
                MessageLog.objects.log(message, RESULT_FAILURE, log_message
                    =str(err))
                deferred += 1
                connection = None
            if _limits_reached(sent, deferred):
                break
            _throttle_emails()
    finally:
        release_lock(lock)
    logging.info('')
    logging.info('%s sent; %s deferred;' % (sent, deferred))
    logging.info('done in %.2f seconds' % (time.time() - start_time))