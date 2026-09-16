def get_snapshots_filename(impl, working_dir):
    snapshots_filename = impl.get_virtual_chain_name() + '.snapshots'
    return os.path.join(working_dir, snapshots_filename)