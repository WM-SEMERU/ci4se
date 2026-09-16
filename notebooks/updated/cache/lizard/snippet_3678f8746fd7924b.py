def do_health_checks(self, list_of_ips):
    threads = []
    results = []
    for count, ip in enumerate(list_of_ips):
        thread = threading.Thread(target=self._do_tcp_check, name='%s:%s' %
            (self.thread_name, ip), args=(ip, results))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return results, []