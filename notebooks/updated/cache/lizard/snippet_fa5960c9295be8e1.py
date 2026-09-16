def segment_kmeans(self, rgb_weight, num_clusters, hue_weight=0.0):
    label_offset = 1
    nonzero_px = np.where(self.data != 0.0)
    nonzero_px = np.c_[nonzero_px[0], nonzero_px[1]]
    color_vals = rgb_weight * self._data[(nonzero_px[:, (0)]), (nonzero_px[
        :, (1)]), :]
    if hue_weight > 0.0:
        hsv_data = cv2.cvtColor(self.data, cv2.COLOR_BGR2HSV)
        color_vals = np.c_[color_vals, hue_weight * hsv_data[(nonzero_px[:,
            (0)]), (nonzero_px[:, (1)]), :1]]
    features = np.c_[nonzero_px, color_vals.astype(np.float32)]
    kmeans = sc.KMeans(n_clusters=num_clusters)
    labels = kmeans.fit_predict(features)
    label_im = np.zeros([self.height, self.width]).astype(np.uint8)
    label_im[nonzero_px[:, (0)], nonzero_px[:, (1)]] = labels + label_offset
    return SegmentationImage(label_im, frame=self.frame)