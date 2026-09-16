def check_alert(self, text):
    try:
        alert = Alert(world.browser)
        if alert.text != text:
            raise AssertionError('Alert text expected to be {!r}, got {!r}.'
                .format(text, alert.text))
    except WebDriverException:
        pass