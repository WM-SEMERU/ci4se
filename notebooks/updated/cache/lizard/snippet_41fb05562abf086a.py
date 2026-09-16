def _update_record(record):
    dt = datetime.fromtimestamp(record.created)
    record.springtime = str(dt)[:-3]
    record.levelname_spring = ('WARN' if record.levelname == 'WARNING' else
        record.levelname)
    record.process_id = str(os.getpid())
    record.thread_name = current_thread().getName()[:15]
    record.logger_name = record.name[:40]
    record.tracing_information = ''
    tracing_information = _tracing_information()
    if tracing_information:
        record.tracing_information = '[' + ','.join(tracing_information) + '] '