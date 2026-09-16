def split_points(self, point_cloud):
    if not isinstance(point_cloud, PointCloud):
        raise ValueError('Can only split point clouds')
    above_plane = point_cloud._data - np.tile(self._x0.data, [1,
        point_cloud.num_points]).T.dot(self._n) > 0
    above_plane = point_cloud.z_coords > 0 & above_plane
    below_plane = point_cloud._data - np.tile(self._x0.data, [1,
        point_cloud.num_points]).T.dot(self._n) <= 0
    below_plane = point_cloud.z_coords > 0 & below_plane
    above_data = point_cloud.data[:, (above_plane)]
    below_data = point_cloud.data[:, (below_plane)]
    return PointCloud(above_data, point_cloud.frame), PointCloud(below_data,
        point_cloud.frame)