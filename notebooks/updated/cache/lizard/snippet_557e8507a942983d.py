def new_from_bundle_config(self, config):
    identity = Identity.from_dict(config['identity'])
    ds = self._db.dataset(identity.vid, exception=False)
    if not ds:
        ds = self._db.new_dataset(**identity.dict)
    b = Bundle(ds, self)
    b.commit()
    b.state = Bundle.STATES.NEW
    b.set_last_access(Bundle.STATES.NEW)
    return b