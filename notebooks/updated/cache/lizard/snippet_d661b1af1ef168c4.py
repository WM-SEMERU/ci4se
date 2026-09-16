def get_announce_filename(working_dir):
    announce_filepath = os.path.join(working_dir,
        get_default_virtualchain_impl().get_virtual_chain_name()) + '.announce'
    return announce_filepath