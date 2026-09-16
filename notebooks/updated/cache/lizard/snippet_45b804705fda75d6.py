def setup_manager_context():
    setup_manager = SetupManager()
    setup_manager.connect_to_game()
    try:
        yield setup_manager
    finally:
        setup_manager.shut_down(kill_all_pids=True)