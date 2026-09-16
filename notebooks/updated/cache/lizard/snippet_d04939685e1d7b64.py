def setup(level: Union[str, int], structured: bool, config_path: str=None):
    global logs_are_structured
    logs_are_structured = structured
    if not isinstance(level, int):
        level = logging._nameToLevel[level]

    def ensure_utf8_stream(stream):
        if not isinstance(stream, io.StringIO) and hasattr(stream, 'buffer'):
            stream = codecs.getwriter('utf-8')(stream.buffer)
            stream.encoding = 'utf-8'
        return stream
    sys.stdout, sys.stderr = (ensure_utf8_stream(s) for s in (sys.stdout,
        sys.stderr))
    logging.basicConfig()
    logging.setLogRecordFactory(NumpyLogRecord)
    if config_path is not None and os.path.isfile(config_path):
        with open(config_path) as fh:
            config = yaml.safe_load(fh)
        for key, val in config.items():
            logging.getLogger(key).setLevel(logging._nameToLevel.get(val,
                level))
    root = logging.getLogger()
    root.setLevel(level)
    if not structured:
        if not sys.stdin.closed and sys.stdout.isatty():
            handler = root.handlers[0]
            handler.setFormatter(AwesomeFormatter())
    else:
        root.handlers[0] = StructuredHandler(level)