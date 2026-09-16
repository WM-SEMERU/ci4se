def _UpdateAndMigrateUnmerged(self, not_merged_stops, zone_map, merge_map,
    schedule):
    for stop, migrated_stop in not_merged_stops:
        if stop.zone_id in zone_map:
            migrated_stop.zone_id = zone_map[stop.zone_id]
        else:
            migrated_stop.zone_id = self.feed_merger.GenerateId(stop.zone_id)
            zone_map[stop.zone_id] = migrated_stop.zone_id
        if stop.parent_station:
            parent_original = schedule.GetStop(stop.parent_station)
            migrated_stop.parent_station = merge_map[parent_original].stop_id
        self.feed_merger.merged_schedule.AddStopObject(migrated_stop)