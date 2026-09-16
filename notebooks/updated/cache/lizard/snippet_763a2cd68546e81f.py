def main(args, stop=False):
    if not stop and not os.path.exists(args.filename):
        sys.stderr.write("'%s' doesn't exists!\n" % args.filename)
        sys.exit(1)
    daemon = FTPMonitorDaemon(con_param=getConParams(settings.
        RABBITMQ_FTP_VIRTUALHOST), queue=settings.RABBITMQ_FTP_INPUT_QUEUE,
        out_exch=settings.RABBITMQ_FTP_EXCHANGE, out_key=settings.
        RABBITMQ_FTP_OUTPUT_KEY, react_fn=None, glob=globals(), fn=args.
        filename if not stop else '')
    if not stop and args.foreground:
        daemon.run()
    else:
        daemon.run_daemon()