def cmd_dataflash_logger(self, args):
    if len(args) == 0:
        print(self.usage())
    elif args[0] == 'status':
        print(self.status())
    elif args[0] == 'stop':
        self.new_log_started = False
        self.stopped = True
    elif args[0] == 'start':
        self.stopped = False
    elif args[0] == 'set':
        self.log_settings.command(args[1:])
    else:
        print(self.usage())