def get_supported_boot_mode(self):
    system = self._get_host_details()
    bios_uefi_class_val = 0
    if 'Bios' in system['Oem']['Hp'] and 'UefiClass' in system['Oem']['Hp'][
        'Bios']:
        bios_uefi_class_val = system['Oem']['Hp']['Bios']['UefiClass']
    return mappings.GET_SUPPORTED_BOOT_MODE_RIS_MAP.get(bios_uefi_class_val)