def run():
    options = btoptions.Options()
    btlog.initialize_logging(options.log_level, options.log_file)
    app = btapp.get_application()
    app.run()