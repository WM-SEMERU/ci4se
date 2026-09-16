def map_vnics(vm):
    return {device.deviceInfo.label: device for device in vm.config.
        hardware.device if isinstance(device, vim.vm.device.
        VirtualEthernetCard)}