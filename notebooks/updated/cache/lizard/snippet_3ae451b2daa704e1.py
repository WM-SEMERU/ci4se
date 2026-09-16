def _worker(self, clf):
    logger.debug(
        'worker %d is running, waiting for tasks from master at rank %d' %
        (MPI.COMM_WORLD.Get_rank(), self.master_rank))
    comm = MPI.COMM_WORLD
    status = MPI.Status()
    while 1:
        task = comm.recv(source=self.master_rank, tag=MPI.ANY_TAG, status=
            status)
        if status.Get_tag():
            break
        comm.send(self._voxel_scoring(task, clf), dest=self.master_rank)