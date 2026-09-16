def restore_bios_config(irmc_info, bios_config):

    def _process_bios_config():
        try:
            if isinstance(bios_config, dict):
                input_data = bios_config
            else:
                input_data = jsonutils.loads(bios_config)
            bios_cfg = input_data['Server']['SystemConfig']['BiosConfig']
            bios_cfg['@Processing'] = 'execute'
            return input_data
        except (TypeError, ValueError, KeyError):
            raise scci.SCCIInvalidInputError(
                'Invalid input bios config "%s".' % bios_config)
    input_data = _process_bios_config()
    try:
        elcm_profile_get(irmc_info=irmc_info, profile_name=PROFILE_BIOS_CONFIG)
        elcm_profile_delete(irmc_info=irmc_info, profile_name=
            PROFILE_BIOS_CONFIG)
    except ELCMProfileNotFound:
        pass
    session = elcm_profile_set(irmc_info=irmc_info, input_data=input_data)
    session_timeout = irmc_info.get('irmc_bios_session_timeout',
        BIOS_CONFIG_SESSION_TIMEOUT)
    _process_session_data(irmc_info=irmc_info, operation='RESTORE_BIOS',
        session_id=session['Session']['Id'], session_timeout=session_timeout)