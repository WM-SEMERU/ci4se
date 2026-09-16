def from_pillow(pil_image):
    pil_image = pil_image.convert('RGB')
    cv2_image = np.array(pil_image)
    cv2_image = cv2_image[:, :, ::-1].copy()
    return cv2_image