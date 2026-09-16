def map_agents(self, stmts, do_rename=True):
    mapped_stmts = []
    num_skipped = 0
    for stmt in stmts:
        mapped_stmt = self.map_agents_for_stmt(stmt, do_rename)
        if mapped_stmt is not None:
            mapped_stmts.append(mapped_stmt)
        else:
            num_skipped += 1
    logger.info('%s statements filtered out' % num_skipped)
    return mapped_stmts