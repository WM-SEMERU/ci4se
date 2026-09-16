def destroy(self, si, logger, session, vcenter_data_model, vm_uuid, vm_name,
    reservation_id):
    self._disconnect_all_my_connectors(session=session, resource_name=
        vm_name, reservation_id=reservation_id, logger=logger)
    vm = self.pv_service.find_by_uuid(si, vm_uuid)
    if vm is not None:
        result = self.pv_service.destroy_vm(vm=vm, logger=logger)
    else:
        logger.info('Could not find the VM {0},will remove the resource.'.
            format(vm_name))
        result = True
    self.resource_remover.remove_resource(session=session,
        resource_full_name=vm_name)
    return result