def randomize(self, device=None, percent=100, silent=False):
    volume = self.get_volume(device)
    blocks = int(volume['size'] / BLOCK_SIZE)
    num_writes = int(blocks * percent * 0.01)
    offsets = sorted(random.sample(range(blocks), num_writes))
    total = 0
    if not silent:
        print('Writing urandom to %s bytes in %s' % (volume['size'], volume
            ['path']))
    with open(volume['path'], 'w') as file:
        for offset in offsets:
            if not silent:
                self.dot()
            file.seek(offset * BLOCK_SIZE)
            data = os.urandom(32768) * 128
            total += len(data)
            file.write(data)
    print('\nWrote: %s' % total)