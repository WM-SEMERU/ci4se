def alltoall(self, x, mesh_axis, split_axis, concat_axis):
    return self._collective_with_groups(x, [mesh_axis], functools.partial(
        alltoall_ring, split_axis=split_axis, concat_axis=concat_axis))