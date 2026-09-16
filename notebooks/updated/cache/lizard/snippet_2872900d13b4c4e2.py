def close(self):
    print('PGPooledTransaction - shutting down connection pool')
    for name, conn in self.pool.iteritems():
        conn.close()
        print('PGPooledTransaction - connection %s closed' % name)