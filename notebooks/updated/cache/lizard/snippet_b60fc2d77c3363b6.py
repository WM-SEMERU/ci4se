def set_updated(self):
    output = []
    for method in self.methods.values():
        data = method['last_output']
        if isinstance(data, list):
            if self.testing and data:
                data[0]['cached_until'] = method.get('cached_until')
            output.extend(data)
        elif data.get('full_text') or 'separator' in data:
            if self.testing:
                data['cached_until'] = method.get('cached_until')
            output.append(data)
    if output != self.last_output:
        urgent = True in [x.get('urgent') for x in output]
        if urgent != self.urgent:
            self.urgent = urgent
        else:
            urgent = False
        self.last_output = output
        self._py3_wrapper.notify_update(self.module_full_name, urgent)