def validate(self):
    for timeperiod, child in self.root.children.items():
        child.validate()
    self.validation_timestamp = datetime.utcnow()