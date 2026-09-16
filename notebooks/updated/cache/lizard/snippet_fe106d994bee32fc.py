def vim_janus(uninstall=None):
    if uninstall is not None:
        uninstall_janus()
    else:
        if not exists('~/.vim/janus'):
            print_msg('not installed => install')
            install_janus()
        else:
            print_msg('already installed => update')
            update_janus()
        customize_janus()
        show_files_used_by_vim_and_janus()