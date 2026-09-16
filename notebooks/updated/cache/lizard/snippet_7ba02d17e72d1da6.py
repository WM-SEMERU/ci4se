def apply_dependencies(self):
    for host in self:
        for parent_id in getattr(host, 'parents', []):
            if parent_id is None:
                continue
            parent = self[parent_id]
            if parent.active_checks_enabled:
                host.act_depend_of.append((parent_id, ['d', 'x', 's', 'f'],
                    '', True))
                parent.act_depend_of_me.append((host.uuid, ['d', 'x', 's',
                    'f'], '', True))
                parent.child_dependencies.add(host.uuid)
                host.parent_dependencies.add(parent_id)