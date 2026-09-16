def start_replication(mysql_settings, binlog_pos_memory=(None, 2), **kwargs):
    if not isinstance(binlog_pos_memory, _bpm.BaseBinlogPosMemory):
        if not isinstance(binlog_pos_memory, (tuple, list)):
            raise ValueError('Invalid binlog position memory: %s' %
                binlog_pos_memory)
        binlog_pos_memory = _bpm.FileBasedBinlogPosMemory(*binlog_pos_memory)
    mysql_settings.setdefault('connect_timeout', 5)
    kwargs.setdefault('blocking', True)
    kwargs.setdefault('resume_stream', True)
    with binlog_pos_memory:
        kwargs.setdefault('log_file', binlog_pos_memory.log_file)
        kwargs.setdefault('log_pos', binlog_pos_memory.log_pos)
        _logger.info('Start replication from %s with:\n%s' % (
            mysql_settings, kwargs))
        start_publishing(mysql_settings, **kwargs)