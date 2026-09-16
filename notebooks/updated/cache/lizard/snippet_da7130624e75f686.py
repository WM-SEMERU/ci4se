def rollback(self):
    return self.component_cache_actor.save(refreshing=self.
        rollback_point_refreshing, next_action=self.
        rollback_point_next_action, json_last_refresh=self.
        rollback_point_last_refresh, data_blob=self.rollback_point_data_blob
        ).get()