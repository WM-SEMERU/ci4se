def encode(precision, with_z):
    logger = logging.getLogger('geobuf')
    stdin = click.get_text_stream('stdin')
    sink = click.get_binary_stream('stdout')
    try:
        data = json.load(stdin)
        pbf = geobuf.encode(data, precision if precision >= 0 else 6, 3 if
            with_z else 2)
        sink.write(pbf)
        sys.exit(0)
    except Exception:
        logger.exception('Failed. Exception caught')
        sys.exit(1)