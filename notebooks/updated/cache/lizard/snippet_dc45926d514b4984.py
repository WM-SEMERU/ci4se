def get_bios_firmware_version(snmp_client):
    try:
        bios_firmware_version = snmp_client.get(BIOS_FW_VERSION_OID)
        return six.text_type(bios_firmware_version)
    except SNMPFailure as e:
        raise SNMPBIOSFirmwareFailure(SNMP_FAILURE_MSG % (
            'GET BIOS FIRMWARE VERSION', e))