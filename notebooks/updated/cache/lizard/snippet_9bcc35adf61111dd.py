def wait_export(self, export_type, timeout=None):
    success = False
    if timeout:
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout
            )
    while not timeout or datetime.datetime.now() < end_time:
        export_description = self.describe_export(export_type)
        if export_type in TALK_EXPORT_TYPES:
            export_metadata = export_description['data_requests'][0]
        else:
            export_metadata = export_description['media'][0]['metadata']
        if export_metadata.get('state', '') in ('ready', 'finished'):
            success = True
            break
        time.sleep(2)
    if not success:
        raise PanoptesAPIException('{}_export not ready within {} seconds'.
            format(export_type, timeout))
    return export_description