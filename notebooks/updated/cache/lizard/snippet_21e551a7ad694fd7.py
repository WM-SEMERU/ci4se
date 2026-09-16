def update_state_active(self):
    self.update_state(self.links[REF_UPDATE_STATE_ACTIVE], {'type': RUN_ACTIVE}
        )
    return self.refresh()