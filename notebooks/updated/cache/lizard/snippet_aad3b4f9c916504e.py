def _log_fail_callback(driver, *args, **kwargs):
    try:
        logs = driver.get_browser_log(levels=[BROWSER_LOG_LEVEL_SEVERE])
        failure_message = ('There were severe console errors on this page: {}'
            .format(logs))
        failure_message = failure_message.replace('{', '{{').replace('}', '}}')
        driver.assertion.assert_false(logs, failure_message=failure_message)
    except (urllib2.URLError, socket.error, WebDriverException):
        pass