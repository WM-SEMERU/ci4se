def normal_cloud_im(self, ksize=3):
    gy = cv2.Sobel(self.data, cv2.CV_64F, 1, 0, ksize=ksize)
    gx = cv2.Sobel(self.data, cv2.CV_64F, 0, 1, ksize=ksize)
    gx_data = gx.reshape(self.height * self.width, 3)
    gy_data = gy.reshape(self.height * self.width, 3)
    pc_grads = np.cross(gx_data, gy_data)
    pc_grad_norms = np.linalg.norm(pc_grads, axis=1)
    pc_grads[pc_grad_norms > 0] = pc_grads[pc_grad_norms > 0] / np.tile(
        pc_grad_norms[pc_grad_norms > 0, np.newaxis], [1, 3])
    pc_grads[pc_grad_norms == 0.0] = np.array([0, 0, -1.0])
    normal_im_data = pc_grads.reshape(self.height, self.width, 3)
    zero_px = self.zero_pixels()
    normal_im_data[(zero_px[:, (0)]), (zero_px[:, (1)]), :] = np.zeros(3)
    return NormalCloudImage(normal_im_data, frame=self.frame)