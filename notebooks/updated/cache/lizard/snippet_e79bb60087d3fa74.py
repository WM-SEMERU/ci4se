def start_monitoring(self):
    time.sleep(1)
    list_of_ips = []
    currently_failed_ips = set()
    currently_questionable_ips = set()
    recheck_failed_interval = 10
    try:
        interval_count = 0
        while not CURRENT_STATE._stop_all:
            start_time = time.time()
            new_ips = self.get_new_working_set()
            if new_ips:
                list_of_ips = new_ips
                currently_failed_ips = set([ip for ip in
                    currently_failed_ips if ip in list_of_ips])
                currently_questionable_ips = set([ip for ip in
                    currently_questionable_ips if ip in list_of_ips])
            live_ips_to_check = [ip for ip in list_of_ips if ip not in
                currently_failed_ips]
            logging.debug('Checking live IPs: %s' % (','.join(
                live_ips_to_check) if live_ips_to_check else '(none alive)'))
            if live_ips_to_check:
                failed_ips, questionable_ips = self.do_health_checks(
                    live_ips_to_check)
                if failed_ips:
                    currently_failed_ips.update(failed_ips)
                    logging.info('Currently failed IPs: %s' % ','.join(
                        currently_failed_ips))
                    self.q_failed_ips.put(list(currently_failed_ips))
                if questionable_ips:
                    currently_questionable_ips.update(failed_ips)
                    logging.info('Currently questionable IPs: %s' % ','.
                        join(currently_questionable_ips))
                    self.q_questionable_ips.put(list(
                        currently_questionable_ips))
            if interval_count == recheck_failed_interval:
                interval_count = 0
                currently_failed_ips = set()
                currently_questionable_ips = set()
            end_time = time.time()
            time.sleep(self.get_monitor_interval() - (end_time - start_time))
            interval_count += 1
        logging.debug('Monitoring loop ended: Global stop')
    except StopReceived:
        return