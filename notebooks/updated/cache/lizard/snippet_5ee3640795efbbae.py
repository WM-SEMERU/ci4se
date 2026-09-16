def is_image_loaded(webdriver, webelement):
    script = u(
        'return arguments[0].complete && type of arguments[0].naturalWidth != "undefined" '
        ) + u('&& arguments[0].naturalWidth > 0')
    try:
        return webdriver.execute_script(script, webelement)
    except:
        return False