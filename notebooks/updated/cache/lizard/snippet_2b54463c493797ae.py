def process():
    invoked_as = os.path.basename(sys.argv[0])
    if invoked_as == 'psiturk':
        launch_shell()
    elif invoked_as == 'psiturk-server':
        launch_server()
    elif invoked_as == 'psiturk-shell':
        launch_shell()
    elif invoked_as == 'psiturk-setup-example':
        setup_example()
    elif invoked_as == 'psiturk-install':
        install_from_exchange()