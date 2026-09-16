def _set_zfcp_config_files(self, fcp, target_wwpn, target_lun):
    host_config = '/sbin/chzdev zfcp-host %s -e' % fcp
    device = '0.0.%s' % fcp
    target = '%s:%s:%s' % (device, target_wwpn, target_lun)
    disk_config = '/sbin/chzdev zfcp-lun %s -e\n' % target
    return '\n'.join((host_config, disk_config))