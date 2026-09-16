def configure_logging(self, context):
    fmt = '%(name)-12s: %(levelname)-8s %(message)s'
    formatter = ANSIFormatter(context, fmt)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logging.root.addHandler(handler)