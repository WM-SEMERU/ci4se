def xmlrpc_save2file(self, filename):
    savefile = open(filename, 'wb')
    try:
        pickle.dump({'scheduled': self.scheduled_tasks, 'reschedule': self.
            reschedule}, savefile)
    except pickle.PicklingError:
        return -1
    savefile.close()
    return 1