def sync_allocations(self):
    vxlan_vnis = set()
    for tun_min, tun_max in self.tunnel_ranges:
        vxlan_vnis |= set(six.moves.range(tun_min, tun_max + 1))
    session = bc.get_writer_session()
    with session.begin(subtransactions=True):
        allocs = session.query(nexus_models_v2.NexusVxlanAllocation
            ).with_lockmode('update').all()
        existing_vnis = set(alloc.vxlan_vni for alloc in allocs)
        vnis_to_remove = [alloc.vxlan_vni for alloc in allocs if alloc.
            vxlan_vni not in vxlan_vnis and not alloc.allocated]
        bulk_size = 100
        chunked_vnis = (vnis_to_remove[i:i + bulk_size] for i in range(0,
            len(vnis_to_remove), bulk_size))
        for vni_list in chunked_vnis:
            session.query(nexus_models_v2.NexusVxlanAllocation).filter(
                nexus_models_v2.NexusVxlanAllocation.vxlan_vni.in_(vni_list)
                ).delete(synchronize_session=False)
        vnis = list(vxlan_vnis - existing_vnis)
        chunked_vnis = (vnis[i:i + bulk_size] for i in range(0, len(vnis),
            bulk_size))
        for vni_list in chunked_vnis:
            bulk = [{'vxlan_vni': vni, 'allocated': False} for vni in vni_list]
            session.execute(nexus_models_v2.NexusVxlanAllocation.__table__.
                insert(), bulk)