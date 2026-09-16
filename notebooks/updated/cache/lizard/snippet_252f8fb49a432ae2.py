def sign_up(self):
    try:
        self.driver.get(self.URL)
        logger.info('Loaded ad page.')
        begin = WebDriverWait(self.driver, 10).until(EC.
            element_to_be_clickable((By.CLASS_NAME, 'btn-primary')))
        begin.click()
        logger.info('Clicked begin experiment button.')
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles
            ) == 2)
        self.driver.switch_to_window(self.driver.window_handles[-1])
        self.driver.set_window_size(1024, 768)
        logger.info('Switched to experiment popup.')
        consent = WebDriverWait(self.driver, 10).until(EC.
            element_to_be_clickable((By.ID, 'consent')))
        consent.click()
        logger.info('Clicked consent button.')
        participate = WebDriverWait(self.driver, 10).until(EC.
            element_to_be_clickable((By.CLASS_NAME, 'btn-success')))
        participate.click()
        logger.info('Clicked start button.')
        return True
    except TimeoutException:
        logger.error('Error during experiment sign up.')
        return False