def new_stats_exporter(options=None, interval=None):
    if options is None:
        _, project_id = google.auth.default()
        options = Options(project_id=project_id)
    if str(options.project_id).strip() == '':
        raise ValueError(ERROR_BLANK_PROJECT_ID)
    ci = client_info.ClientInfo(client_library_version=get_user_agent_slug())
    client = monitoring_v3.MetricServiceClient(client_info=ci)
    exporter = StackdriverStatsExporter(client=client, options=options)
    transport.get_exporter_thread(stats.stats, exporter, interval=interval)
    return exporter