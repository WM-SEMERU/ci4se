def send_loop():
    while True:
        while not Message.objects.all():
            logging.debug(
                'sleeping for %s seconds before checking queue again' %
                EMPTY_QUEUE_SLEEP)
            time.sleep(EMPTY_QUEUE_SLEEP)
        send_all()