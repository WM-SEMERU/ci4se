def interactive(self, bConfirmQuit=True, bShowBanner=True):
    print('')
    print('-' * 79)
    print('Interactive debugging session started.')
    print('Use the "help" command to list all available commands.')
    print('Use the "quit" command to close this session.')
    print('-' * 79)
    if self.lastEvent is None:
        print('')
    console = ConsoleDebugger()
    console.confirm_quit = bConfirmQuit
    console.load_history()
    try:
        console.start_using_debugger(self)
        console.loop()
    finally:
        console.stop_using_debugger()
        console.save_history()
    print('')
    print('-' * 79)
    print('Interactive debugging session closed.')
    print('-' * 79)
    print('')