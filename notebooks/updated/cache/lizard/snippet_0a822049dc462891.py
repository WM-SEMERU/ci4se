def exception_handler(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        pypro.console.out('')
        pypro.console.err('Canceled')
    elif exctype == PyproException:
        pypro.console.err('[Error] ', value.message)
        exit()
    else:
        sys.__excepthook__(exctype, value, traceback)