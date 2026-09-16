def _xfer_file(self, source_file=None, source_config=None, dest_file=None,
    file_system=None, TransferClass=FileTransfer):
    if not source_file and not source_config:
        raise ValueError('File source not specified for transfer.')
    if not dest_file or not file_system:
        raise ValueError('Destination file or file system not specified.')
    if source_file:
        kwargs = dict(ssh_conn=self.device, source_file=source_file,
            dest_file=dest_file, direction='put', file_system=file_system)
    elif source_config:
        kwargs = dict(ssh_conn=self.device, source_config=source_config,
            dest_file=dest_file, direction='put', file_system=file_system)
    enable_scp = True
    if self.inline_transfer:
        enable_scp = False
    with TransferClass(**kwargs) as transfer:
        if transfer.check_file_exists() and transfer.compare_md5():
            msg = 'File already exists and has correct MD5: no SCP needed'
            return True, msg
        if not transfer.verify_space_available():
            msg = 'Insufficient space available on remote device'
            return False, msg
        if enable_scp:
            transfer.enable_scp()
        transfer.transfer_file()
        if transfer.verify_file():
            msg = 'File successfully transferred to remote device'
            return True, msg
        else:
            msg = 'File transfer to remote device failed'
            return False, msg
        return False, ''