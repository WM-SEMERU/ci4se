def process_request(self, request, client_address):
    t = threading.Thread(target=self.process_request_thread, args=(request,
        client_address), name='PailgunRequestThread')
    t.daemon = self.daemon_threads
    t.start()