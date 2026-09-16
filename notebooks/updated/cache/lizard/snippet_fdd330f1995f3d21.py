def cmd_fw(self, args):
    if len(args) == 0:
        print(self.usage())
        return
    rest = args[1:]
    if args[0] == 'manifest':
        self.cmd_fw_manifest(rest)
    elif args[0] == 'list':
        self.cmd_fw_list(rest)
    elif args[0] == 'download':
        self.cmd_fw_download(rest)
    elif args[0] in ['help', 'usage']:
        self.cmd_fw_help(rest)
    else:
        print(self.usage())