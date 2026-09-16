def patStarLines(s0):
    arr = np.zeros((s0, s0), dtype=np.uint8)
    col = 255
    t = int(s0 / 100.0)
    for pos in np.linspace(0, np.pi / 2, 15):
        p0 = int(round(np.sin(pos) * s0 * 2))
        p1 = int(round(np.cos(pos) * s0 * 2))
        cv2.line(arr, (0, 0), (p0, p1), color=col, thickness=t, lineType=
            cv2.LINE_AA)
    return arr.astype(float)