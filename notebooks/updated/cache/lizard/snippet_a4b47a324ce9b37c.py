def start_executing_svc_checks(self):
    if not self.my_conf.execute_service_checks:
        self.my_conf.modified_attributes |= DICT_MODATTR[
            'MODATTR_ACTIVE_CHECKS_ENABLED'].value
        self.my_conf.execute_service_checks = True
        self.my_conf.explode_global_conf()
        self.daemon.update_program_status()