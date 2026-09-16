def _call_exception_handlers(exception):
    for handler in EXCEPTION_HANDLERS:
        try:
            if handler.wants(exception):
                handler.handle(exception)
        except:
            try:
                logging.error(traceback.format_exc())
            except:
                pass