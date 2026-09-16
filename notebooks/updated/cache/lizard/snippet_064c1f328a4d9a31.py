def progress(progress):
    if isinstance(progress, int) or isinstance(progress, float):
        progress = float(progress)
    else:
        try:
            progress = float(json.loads(progress))
        except (TypeError, ValueError):
            return warning('Progress must be a float.')
    if not 0 <= progress <= 1:
        return warning('Progress must be a float between 0 and 1.')
    return json.dumps({'proc.progress': progress})