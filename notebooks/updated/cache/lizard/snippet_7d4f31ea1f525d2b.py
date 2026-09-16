def run_experiment(self):
    try:
        self.sign_up()
        self.participate()
        if self.sign_off():
            self.complete_experiment('worker_complete')
        else:
            self.complete_experiment('worker_failed')
    finally:
        self.driver.quit()