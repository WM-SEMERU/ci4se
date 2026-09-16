def get_snapshots(self, si, logger, vm_uuid):
    vm = self.pyvmomi_service.find_by_uuid(si, vm_uuid)
    logger.info('Get snapshots')
    snapshots = SnapshotRetriever.get_vm_snapshots(vm)
    return snapshots.keys()