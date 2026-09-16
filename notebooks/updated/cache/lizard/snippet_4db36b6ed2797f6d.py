def calc_signal_sum(self, measure='LFP'):
    if self.RANK_CELLINDICES.size > 0:
        for i, cellindex in enumerate(self.RANK_CELLINDICES):
            if i == 0:
                data = self.output[cellindex][measure]
            else:
                data += self.output[cellindex][measure]
    else:
        data = np.zeros((len(self.electrodeParams['x']), self.cellParams[
            'tstopms'] / self.dt_output + 1), dtype=np.float32)
    if RANK == 0:
        DATA = np.zeros_like(data, dtype=np.float32)
    else:
        DATA = None
    COMM.Reduce(data, DATA, op=MPI.SUM, root=0)
    return DATA