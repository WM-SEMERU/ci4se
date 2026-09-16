def do_transform(self):
    if not self.transform:
        return
    try:
        self.latest_value = utils.Transform(expr=self.transform, value=self
            .latest_value, timedelta=self.time_between_updates().
            total_seconds()).result()
    except (TypeError, ValueError):
        logger.warn("Invalid transformation '%s' for metric %s", self.
            transfrom, self.pk)
    self.transform = ''