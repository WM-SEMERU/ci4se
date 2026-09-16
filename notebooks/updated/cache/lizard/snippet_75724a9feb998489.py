def remove_port_profile_to_delete(self, profile_name, device_id):
    with self.session.begin(subtransactions=True):
        self.session.query(ucsm_model.PortProfileDelete).filter_by(profile_id
            =profile_name, device_id=device_id).delete()