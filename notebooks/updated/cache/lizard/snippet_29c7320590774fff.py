def monitor(ctx, details):
    ingest_config_obj(ctx, silent=False)
    show_colors = ctx.obj['show_color']
    event_display = {JobEventName.Started: {'color': 'blue', 'label':
        'started'}, JobEventName.Succeeded: {'color': 'green', 'label':
        'succeeded'}, JobEventName.Stopped: {'color': 'yellow', 'label':
        'stopped'}, JobEventName.Aborted: {'color': 'red', 'label': 'aborted'}}
    click.echo('\n')
    click.echo('{:>10} {:>12} {:25} {:18} {:16} {:28} {}'.format('Status',
        'Type', 'Name', 'Duration (sec)', 'Queue' if details else '', 
        'Workflow ID' if details else '', 'Worker' if details else ''))
    click.echo('-' * (136 if details else 65))
    for event in workflow_events(ctx.obj['config']):
        evt_disp = event_display[event.event]
        click.echo('{:>{}} {:>{}} {:25} {:18} {:16} {:28} {}'.format(_style
            (show_colors, evt_disp['label'], fg=evt_disp['color']), 20 if
            show_colors else 10, _style(show_colors, event.type, bold=True,
            fg=JOB_COLOR[event.type]), 24 if show_colors else 12, event.
            name, '{0:.3f}'.format(event.duration) if event.duration is not
            None else '', event.queue if details else '', event.workflow_id if
            details else '', event.hostname if details else ''))