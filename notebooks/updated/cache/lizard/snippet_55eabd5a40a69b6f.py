def report_data(self, entity_data):
    try:
        response = None
        response = self.client.post(self.__data_url(), data=self.to_json(
            entity_data), headers={'Content-Type': 'application/json'},
            timeout=0.8)
        if response.status_code is 200:
            self.last_seen = datetime.now()
    except (requests.ConnectTimeout, requests.ConnectionError):
        logger.debug('report_data: host agent connection error')
    finally:
        return response