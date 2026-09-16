def project_and_to2dim_ordered_indices(self, pps, plane_center='mean'):
    pp2d = self.project_and_to2dim(pps, plane_center)
    return anticlockwise_sort_indices(pp2d)