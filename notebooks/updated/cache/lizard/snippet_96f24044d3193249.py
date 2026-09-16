def process_pad_frame(self, id=None, msg=None):
    df = json_normalize(msg)
    dt = json.loads(df.to_json())
    flat_msg = {}
    for k in dt:
        new_key = 'pad_{}'.format(k)
        flat_msg[new_key] = dt[k]['0']
        if new_key not in self.pad_keys:
            self.pad_keys[new_key] = k
    dt['pad_id'] = id
    self.all_pad.append(dt)
    log.debug('PAD data updated:')
    log.debug(self.pad_keys)
    log.debug(self.all_pad)
    log.debug('')
    return flat_msg