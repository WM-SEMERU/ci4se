def export(self, name, columns, points):
    for i in range(len(columns)):
        if not isinstance(points[i], Number):
            continue
        stat_name = '{}.{}.{}'.format(self.prefix, name, columns[i])
        stat_value = points[i]
        tags = self.parse_tags(self.tags)
        try:
            self.client.send(stat_name, stat_value, **tags)
        except Exception as e:
            logger.error('Can not export stats %s to OpenTSDB (%s)' % (name, e)
                )
    logger.debug('Export {} stats to OpenTSDB'.format(name))