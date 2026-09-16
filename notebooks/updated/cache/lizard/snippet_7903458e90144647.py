def _show_corners(self, image, corners):
    temp = image
    cv2.drawChessboardCorners(temp, (self.rows, self.columns), corners, True)
    window_name = 'Chessboard'
    cv2.imshow(window_name, temp)
    if cv2.waitKey(0):
        cv2.destroyWindow(window_name)