def generate_traffic(self, start_page, destination_page, loops=1):
    for loop in range(loops):
        self.generate_referral(start_page, destination_page)
        time.sleep(0.05)