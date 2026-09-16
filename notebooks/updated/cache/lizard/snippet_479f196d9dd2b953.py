def track_execution(cmd, project, experiment, **kwargs):
    runner = RunInfo(cmd=cmd, project=project, experiment=experiment, **kwargs)
    yield runner
    runner.commit()