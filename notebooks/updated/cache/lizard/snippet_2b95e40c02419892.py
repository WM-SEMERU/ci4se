def restart(self, key):
    if key in self.queue:
        if self.queue[key]['status'] in ['failed', 'done']:
            new_entry = {'command': self.queue[key]['command'], 'path':
                self.queue[key]['path']}
            self.add_new(new_entry)
            self.write()
            return True
    return False