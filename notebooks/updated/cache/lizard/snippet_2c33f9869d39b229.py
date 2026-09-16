def extend_settings(self, data_id, files, secrets):
    data = Data.objects.select_related('process').get(pk=data_id)
    files[ExecutorFiles.DJANGO_SETTINGS].update({'USE_TZ': settings.USE_TZ,
        'FLOW_EXECUTOR_TOOLS_PATHS': self.get_tools_paths()})
    files[ExecutorFiles.DATA] = model_to_dict(data)
    files[ExecutorFiles.DATA_LOCATION] = model_to_dict(data.location)
    files[ExecutorFiles.PROCESS] = model_to_dict(data.process)
    files[ExecutorFiles.PROCESS]['resource_limits'
        ] = data.process.get_resource_limits()
    secrets.update(data.resolve_secrets())