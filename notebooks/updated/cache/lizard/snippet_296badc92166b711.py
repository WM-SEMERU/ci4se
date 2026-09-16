def stack_images(image_list, wht_list, sigma_list):
    image_stacked = np.zeros_like(image_list[0])
    wht_stacked = np.zeros_like(image_stacked)
    sigma_stacked = 0.0
    for i in range(len(image_list)):
        image_stacked += image_list[i] * wht_list[i]
        sigma_stacked += sigma_list[i] ** 2 * np.median(wht_list[i])
        wht_stacked += wht_list[i]
    image_stacked /= wht_stacked
    sigma_stacked /= np.median(wht_stacked)
    wht_stacked /= len(wht_list)
    return image_stacked, wht_stacked, np.sqrt(sigma_stacked)