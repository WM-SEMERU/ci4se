def process_dns_frame(self, id=None, msg=None):
    df = json_normalize(msg)
    dt = json.loads(df.to_json())
    flat_msg = {}
    for k in dt:
        new_key = 'dns_{}'.format(k)
        flat_msg[new_key] = dt[k]['0']
        if new_key not in self.dns_keys:
            self.dns_keys[new_key] = k
    dt['dns_id'] = id
    self.all_dns.append(dt)
    log.debug('DNS data updated:')
    log.debug(self.dns_keys)
    log.debug(self.all_dns)
    log.debug('')
    return flat_msg