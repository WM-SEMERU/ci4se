def process(self):
    threads = []
    for client in self.find_clients(self.hostnames):
        print(client)
        thread = threading.Thread(target=self._process_thread, args=(client,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()