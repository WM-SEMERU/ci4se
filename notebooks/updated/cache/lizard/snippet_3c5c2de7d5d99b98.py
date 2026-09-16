def collect(self):
    instances = {}
    for device in os.listdir('/dev/'):
        instances.update(self.match_device(device, '/dev/'))
    for device_id in os.listdir('/dev/disk/by-id/'):
        instances.update(self.match_device(device, '/dev/disk/by-id/'))
    metrics = {}
    for device, p in instances.items():
        output = p.communicate()[0].strip()
        try:
            metrics[device + '.Temperature'] = float(output)
        except:
            self.log.warn('Disk temperature retrieval failed on ' + device)
    for metric in metrics.keys():
        self.publish(metric, metrics[metric])