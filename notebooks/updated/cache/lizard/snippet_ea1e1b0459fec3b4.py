def _checkpoint(self, stage):
    if stage is None:
        return False
    try:
        is_checkpoint = stage.checkpoint
    except AttributeError:
        if hasattr(stage, '__call__'):
            stage = stage.__name__
        else:
            base, ext = os.path.splitext(stage)
            if ext and '.' not in base:
                print(
                    "WARNING: '{}' looks like it may be the name or path of a file; for such a checkpoint, use touch_checkpoint."
                    .format(stage))
    else:
        if not is_checkpoint:
            print('Not a checkpoint: {}'.format(stage))
            return False
        stage = stage.name
    print("Checkpointing: '{}'".format(stage))
    if os.path.isabs(stage):
        check_fpath = stage
    else:
        check_fpath = checkpoint_filepath(stage, pm=self)
    return self._touch_checkpoint(check_fpath)