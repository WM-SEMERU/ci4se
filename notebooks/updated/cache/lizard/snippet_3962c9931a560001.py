def draw_text(img, pos, text, color, font_scale=0.4):
    img = img.astype(np.uint8)
    x0, y0 = int(pos[0]), int(pos[1])
    font = cv2.FONT_HERSHEY_SIMPLEX
    (text_w, text_h), _ = cv2.getTextSize(text, font, font_scale, 1)
    if x0 + text_w > img.shape[1]:
        x0 = img.shape[1] - text_w
    if y0 - int(1.15 * text_h) < 0:
        y0 = int(1.15 * text_h)
    back_topleft = x0, y0 - int(1.3 * text_h)
    back_bottomright = x0 + text_w, y0
    cv2.rectangle(img, back_topleft, back_bottomright, color, -1)
    text_bottomleft = x0, y0 - int(0.25 * text_h)
    cv2.putText(img, text, text_bottomleft, font, font_scale, (222, 222, 
        222), lineType=cv2.LINE_AA)
    return img