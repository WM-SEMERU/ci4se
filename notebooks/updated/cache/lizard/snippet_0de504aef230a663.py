def format(self, record):
    if record.levelno == logging.DEBUG:
        string = Back.WHITE + Fore.BLACK + ' debug '
    elif record.levelno == logging.INFO:
        string = Back.BLUE + Fore.WHITE + ' info '
    elif record.levelno == logging.WARNING:
        string = Back.YELLOW + Fore.BLACK + ' warning '
    elif record.levelno == logging.ERROR:
        string = Back.RED + Fore.WHITE + ' error '
    elif record.levelno == logging.CRITICAL:
        string = Back.BLACK + Fore.WHITE + ' critical '
    else:
        string = ''
    return '{none}{string}{none} {super}'.format(none=Style.RESET_ALL,
        string=string, super=super().format(record))