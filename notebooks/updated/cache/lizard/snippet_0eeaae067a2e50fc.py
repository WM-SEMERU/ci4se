def _gather_local_posterior(self, use_gather, gather_size, gather_offset):
    if use_gather:
        self.comm.Gather(self.local_posterior_, self.gather_posterior, root=0)
    else:
        target = [self.gather_posterior, gather_size, gather_offset, MPI.DOUBLE
            ]
        self.comm.Gatherv(self.local_posterior_, target)
    return self