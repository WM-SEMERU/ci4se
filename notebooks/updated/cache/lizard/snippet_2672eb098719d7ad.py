def qapplication(translate=True, test_time=3):
    if running_in_mac_app():
        SpyderApplication = MacApplication
    else:
        SpyderApplication = QApplication
    app = SpyderApplication.instance()
    if app is None:
        app = SpyderApplication(['Spyder'])
        app.setApplicationName('Spyder')
    if translate:
        install_translator(app)
    test_ci = os.environ.get('TEST_CI_WIDGETS', None)
    if test_ci is not None:
        timer_shutdown = QTimer(app)
        timer_shutdown.timeout.connect(app.quit)
        timer_shutdown.start(test_time * 1000)
    return app