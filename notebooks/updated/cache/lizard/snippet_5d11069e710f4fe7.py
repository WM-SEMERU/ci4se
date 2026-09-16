def initialize_from_checkpoint(state):
    model_paths = glob.glob(os.path.join(FLAGS.checkpoint_dir,
        'work_dir/model.ckpt-*.pb'))
    if len(model_paths) != 1:
        raise RuntimeError(
            'Expected exactly one model in the checkpoint work_dir, got [{}]'
            .format(', '.join(model_paths)))
    start_model_path = model_paths[0]
    state.best_model_name = 'checkpoint'
    shutil.copy(start_model_path, os.path.join(fsdb.models_dir(), state.
        best_model_name + '.pb'))
    golden_chunks_dir = os.path.join(FLAGS.checkpoint_dir, 'golden_chunks')
    for basename in os.listdir(golden_chunks_dir):
        path = os.path.join(golden_chunks_dir, basename)
        shutil.copy(path, fsdb.golden_chunk_dir())
    work_dir = os.path.join(FLAGS.checkpoint_dir, 'work_dir')
    for basename in os.listdir(work_dir):
        path = os.path.join(work_dir, basename)
        shutil.copy(path, fsdb.working_dir())