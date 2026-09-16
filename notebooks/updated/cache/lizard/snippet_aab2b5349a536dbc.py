def _find_newest_ckpt(ckpt_dir):
    full_paths = [os.path.join(ckpt_dir, fname) for fname in os.listdir(
        ckpt_dir) if fname.startswith('experiment_state') and fname.
        endswith('.json')]
    return max(full_paths)