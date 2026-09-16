def file_transfer(ssh_conn, source_file, dest_file, file_system=None,
    direction='put', disable_md5=False, inline_transfer=False,
    overwrite_file=False):
    transferred_and_verified = {'file_exists': True, 'file_transferred':
        True, 'file_verified': True}
    transferred_and_notverified = {'file_exists': True, 'file_transferred':
        True, 'file_verified': False}
    nottransferred_but_verified = {'file_exists': True, 'file_transferred':
        False, 'file_verified': True}
    if ('cisco_ios' in ssh_conn.device_type or 'cisco_xe' in ssh_conn.
        device_type):
        cisco_ios = True
    else:
        cisco_ios = False
    if not cisco_ios and inline_transfer:
        raise ValueError(
            'Inline Transfer only supported for Cisco IOS/Cisco IOS-XE')
    scp_args = {'ssh_conn': ssh_conn, 'source_file': source_file,
        'dest_file': dest_file, 'direction': direction}
    if file_system is not None:
        scp_args['file_system'] = file_system
    TransferClass = InLineTransfer if inline_transfer else FileTransfer
    with TransferClass(**scp_args) as scp_transfer:
        if scp_transfer.check_file_exists():
            if overwrite_file:
                if not disable_md5:
                    if scp_transfer.compare_md5():
                        return nottransferred_but_verified
                    else:
                        verifyspace_and_transferfile(scp_transfer)
                        if scp_transfer.compare_md5():
                            return transferred_and_verified
                        else:
                            raise ValueError(
                                'MD5 failure between source and destination files'
                                )
                else:
                    verifyspace_and_transferfile(scp_transfer)
                    return transferred_and_notverified
            else:
                if not disable_md5:
                    if scp_transfer.compare_md5():
                        return nottransferred_but_verified
                msg = 'File already exists and overwrite_file is disabled'
                raise ValueError(msg)
        else:
            verifyspace_and_transferfile(scp_transfer)
            if not disable_md5:
                if scp_transfer.compare_md5():
                    return transferred_and_verified
                else:
                    raise ValueError(
                        'MD5 failure between source and destination files')
            else:
                return transferred_and_notverified