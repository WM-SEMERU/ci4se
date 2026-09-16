def find_text_color(base_color, dark_color='black', light_color='white',
    coef_choice=0):
    coef_options = [np.array((0.241, 0.691, 0.068, 0)), np.array((0.299, 
        0.587, 0.114, 0))]
    coefs = coef_options[coef_choice]
    rgb = np.array(base_color) * 255
    brightness = np.sqrt(np.dot(coefs, rgb ** 2))
    if brightness > 130:
        return dark_color
    return light_color