def find_chessboard(self, sx=6, sy=9):
    criteria = cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001
    objp = np.zeros((sx * sy, 3), np.float32)
    objp[:, :2] = np.mgrid[0:sx, 0:sy].T.reshape(-1, 2)
    objpoints = []
    imgpoints = []
    img = self.data.astype(np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ret, corners = cv2.findChessboardCorners(gray, (sx, sy), None)
    if ret:
        objpoints.append(objp)
        cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)
        if corners is not None:
            return corners.squeeze()
    return None