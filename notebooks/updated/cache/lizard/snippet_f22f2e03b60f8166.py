def is_instance_throughput_too_low(self, inst_id):
    r = self.instance_throughput_ratio(inst_id)
    if r is None:
        logger.debug('{} instance {} throughput is not measurable.'.format(
            self, inst_id))
        return None
    too_low = r < self.Delta
    if too_low:
        logger.display(
            '{}{} instance {} throughput ratio {} is lower than Delta {}.'.
            format(MONITORING_PREFIX, self, inst_id, r, self.Delta))
    else:
        logger.trace('{} instance {} throughput ratio {} is acceptable.'.
            format(self, inst_id, r))
    return too_low