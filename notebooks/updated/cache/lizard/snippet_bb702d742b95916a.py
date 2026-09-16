def replicate(self, dst_lun_id, max_time_out_of_sync, replication_name=None,
    replicate_existing_snaps=None, remote_system=None):
    return UnityReplicationSession.create(self._cli, self.get_id(),
        dst_lun_id, max_time_out_of_sync, name=replication_name,
        replicate_existing_snaps=replicate_existing_snaps, remote_system=
        remote_system)