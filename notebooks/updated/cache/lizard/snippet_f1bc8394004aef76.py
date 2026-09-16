def get_screen():
    img_title = 'screen_' + g.client_id + '.png'
    image_path = STATIC_FILES_PATH + img_title
    if g.driver_status != WhatsAPIDriverStatus.LoggedIn:
        try:
            g.driver.get_qr(image_path)
            return send_file(image_path, mimetype='image/png')
        except Exception as err:
            pass
    g.driver.screenshot(image_path)
    return send_file(image_path, mimetype='image/png')