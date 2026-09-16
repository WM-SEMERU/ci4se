def print_statements(self):
    logger.info('--- Direct INDRA statements ----------')
    for i, stmt in enumerate(self.statements):
        logger.info('%s: %s' % (i, stmt))
    logger.info('--- Indirect INDRA statements ----------')
    for i, stmt in enumerate(self.indirect_stmts):
        logger.info('%s: %s' % (i, stmt))