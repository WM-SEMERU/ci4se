def brightness(im):
    im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(im_hsv)
    height, weight = v.shape[:2]
    total_bright = 0
    for i in v:
        total_bright = total_bright + sum(i)
    return float(total_bright) / (height * weight)