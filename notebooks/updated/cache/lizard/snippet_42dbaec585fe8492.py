def set_iscsi_initiator_info(self, initiator_iqn):
    if self._is_boot_mode_uefi() is True:
        iscsi_uri = self._check_iscsi_rest_patch_allowed()
        initiator_info = {'iSCSIInitiatorName': initiator_iqn}
        status, headers, response = self._rest_patch(iscsi_uri, None,
            initiator_info)
        if status >= 300:
            msg = self._get_extended_error(response)
            raise exception.IloError(msg)
    else:
        msg = 'iSCSI initiator cannot be set in the BIOS boot mode'
        raise exception.IloCommandNotSupportedError(msg)