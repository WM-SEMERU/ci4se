def run():
    print('Environment', os.environ)
    try:
        os.environ['SELENIUM']
    except KeyError:
        print('Please set the environment variable SELENIUM to Selenium URL')
        sys.exit(1)
    driver = WhatsAPIDriver(client='remote', command_executor=os.environ[
        'SELENIUM'])
    print('Waiting for QR')
    driver.wait_for_login()
    print('Bot started')
    driver.subscribe_new_messages(NewMessageObserver())
    print('Waiting for new messages...')
    while True:
        time.sleep(60)