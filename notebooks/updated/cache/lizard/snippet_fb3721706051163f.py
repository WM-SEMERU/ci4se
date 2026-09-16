def refresh(self, wait_for_active=False, retry_seconds=5):
    done = False
    while not done:
        response = self.layer2.describe_table(self.name)
        self.update_from_response(response)
        if wait_for_active:
            if self.status == 'ACTIVE':
                done = True
            else:
                time.sleep(retry_seconds)
        else:
            done = True