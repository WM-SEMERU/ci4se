def check_orphaned(self):
    orphans_count = {}
    now = int(time.time())
    actions = list(self.checks.values()) + list(self.actions.values())
    for chk in actions:
        if chk.status not in [ACT_STATUS_POLLED]:
            continue
        time_to_orphanage = self.find_item_by_id(chk.ref
            ).get_time_to_orphanage()
        if not time_to_orphanage:
            continue
        if chk.t_to_go > now - time_to_orphanage:
            continue
        logger.info('Orphaned %s (%d s / %s / %s) check for: %s (%s)', chk.
            is_a, time_to_orphanage, chk.t_to_go, now, self.find_item_by_id
            (chk.ref).get_full_name(), chk)
        chk._is_orphan = True
        chk.status = ACT_STATUS_SCHEDULED
        if chk.my_worker not in orphans_count:
            orphans_count[chk.my_worker] = 0
        orphans_count[chk.my_worker] += 1
    for sta_name in orphans_count:
        logger.warning(
            "%d actions never came back for the satellite '%s'. I reenable them for polling."
            , orphans_count[sta_name], sta_name)